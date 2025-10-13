import streamlit as st
import pandas as pd
import numpy as np
import re
import os
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="IMDB Movies EDA", layout="wide")

# -------------------------
# Initialize Session State
# -------------------------
if 'section' not in st.session_state:
    st.session_state.section = None
if 'reset_filters' not in st.session_state:
    st.session_state.reset_filters = False
if 'first_load' not in st.session_state:
    st.session_state.first_load = True

# -------------------------
# Load Dataset
# -------------------------
@st.cache_data
def load_data():
    # Define the expected filename
    file_name = "imdb_top_1000.csv"

    # Check if the file exists in the current directory
    if not os.path.exists(file_name):
         st.error(f"CSV file not found: '{file_name}'. Please ensure the file is in the same directory as your Streamlit script.")
         st.stop() # Stop execution if file is not found
         return pd.DataFrame() # Return empty dataframe

    df = pd.read_csv(file_name)
    df.columns = df.columns.str.lower()

    # Convert released_year to integer format
    df['released_year'] = pd.to_numeric(df['released_year'], errors='coerce').astype('Int64')

    # Fix runtime column - extract numeric values from strings like "142 min"
    def extract_runtime(runtime_str):
        if pd.isna(runtime_str):
            return np.nan
        # Extract numbers from the string
        numbers = re.findall(r'\d+', str(runtime_str))
        if numbers:
            return int(numbers[0])
        return np.nan

    df['runtime'] = df['runtime'].apply(extract_runtime)
    df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')

    # Check if meta_score exists before processing
    if 'meta_score' in df.columns:
        df['meta_score'] = pd.to_numeric(df['meta_score'], errors='coerce') # Ensure meta_score is numeric
    else:
        df['meta_score'] = np.nan

    if 'no_of_votes' in df.columns:
        df['no_of_votes'] = pd.to_numeric(df['no_of_votes'], errors='coerce') # Ensure no_of_votes is numeric
    else:
        df['no_of_votes'] = np.nan

    # Convert 'Gross' to numeric, removing commas first
    if 'gross' in df.columns:
        df['gross'] = df['gross'].astype(str).str.replace(',', '') # Removed errors='ignore'
        df['gross'] = pd.to_numeric(df['gross'], errors='coerce')
    else:
        df['gross'] = np.nan

    # Handle missing values
    if 'certificate' in df.columns:
        df['certificate'] = df['certificate'].fillna('Unrated')
    else:
        df['certificate'] = 'Unrated'

    if 'meta_score' in df.columns:
        df['meta_score'] = df['meta_score'].fillna(df['meta_score'].mean())

    if 'gross' in df.columns:
        df['gross'] = df['gross'].fillna(df['gross'].median())

    # Create sequel column
    def check_sequel(title):
        title = str(title).lower()
        keywords = ["part", "chapter", "episode", "ii", "iii", "iv", "v", "vi",
                    "2", "3", "4", "5", "6", "7", "8", "9"]
        return any(k in title for k in keywords)

    df['is_sequel'] = df['series_title'].apply(check_sequel)

    # Create year categories
    def categorize_year(y):
        if pd.isna(y):
            return "Unknown"
        if y < 1980:
            return "🎞️ Old (Pre-1980)"
        elif y < 2000:
            return "📀 Classic (1980-1999)"
        elif y < 2015:
            return "🎬 Modern (2000-2014)"
        else:
            return "🆕 Recent (2015+)"

    df['year_group'] = df['released_year'].apply(categorize_year)

    # Create genre categories
    def categorize_genre(g):
        g = str(g).lower()
        if "comedy" in g:
            return "😂 Comedy"
        elif "drama" in g:
            return "🎭 Drama"
        elif "action" in g:
            return "💥 Action"
        elif "horror" in g or "thriller" in g:
            return "👻 Horror/Thriller"
        elif "sci-fi" in g or "fantasy" in g:
            return "🌌 Sci-Fi/Fantasy"
        elif "animation" in g or "family" in g:
            return "👪 Family/Animation"
        elif "romance" in g:
            return "❤️ Romance"
        elif "musical" in g:
            return "🎶 Musical/Other"
        else:
            return "🎶 Other"

    df['genre_group'] = df['genre'].apply(categorize_genre)

    # Create certificate categories
    def categorize_certificate(c):
        if pd.isna(c) or c == "Unrated":
            return "❓ Unrated/Other"
        c = str(c).upper()
        if c in ["U", "UA", "PG", "G"]:
            return "👨‍👩‍👧‍👦 Family-Friendly"
        elif c in ["PG-13", "12A", "15"]:
            return "🎯 Teens"
        elif c in ["R", "A", "NC-17"]:
            return "🔞 Adults"
        else:
            return "❓ Unrated/Other"

    df['certificate_group'] = df['certificate'].apply(categorize_certificate)

    return df

df = load_data()

# Initialize filter session states before any widgets are created
if 'genre_filter' not in st.session_state:
    st.session_state.genre_filter = []
if 'certificate_filter' not in st.session_state:
    st.session_state.certificate_filter = []
if 'year_filter' not in st.session_state:
    year_min = int(df['released_year'].min(skipna=True)) if pd.notna(df['released_year'].min(skipna=True)) else 1900
    year_max = int(df['released_year'].max(skipna=True)) if pd.notna(df['released_year'].max(skipna=True)) else 2025
    st.session_state.year_filter = (year_min, year_max)
if 'rating_filter' not in st.session_state:
    rating_min = float(df['imdb_rating'].min(skipna=True)) if pd.notna(df['imdb_rating'].min(skipna=True)) else 0.0
    rating_max = float(df['imdb_rating'].max(skipna=True)) if pd.notna(df['imdb_rating'].max(skipna=True)) else 10.0
    st.session_state.rating_filter = (rating_min, rating_max)
if 'runtime_filter' not in st.session_state:
    runtime_min = int(df['runtime'].min(skipna=True)) if not pd.isna(df['runtime'].min(skipna=True)) else 0
    runtime_max = int(df['runtime'].max(skipna=True)) if not pd.isna(df['runtime'].max(skipna=True)) else 180
    st.session_state.runtime_filter = (runtime_min, runtime_max)
if 'meta_score_filter' not in st.session_state:
    st.session_state.meta_score_filter = (0, 100)  # Default range for meta score
if 'actor_filter' not in st.session_state:
    st.session_state.actor_filter = []


# -------------------------
# Background Gradient + Top-Right GIF + Top-Left GIF
# -------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #f0f4f8, #d9e2ec);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .top-right-gif {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 999;
    }
    .top-left-gif {
        position: fixed;
        top: 10px;
        left: 10px;
        z-index: 999;
    }
    .gradient-button {
        width: 100%; /* Adjusted width for better fit in columns */
        background: linear-gradient(90deg, #ff7e5f, #feb47b, #86A8E7, #91EAE4);
        border: none;
        color: white;
        padding: 15px 0;
        text-align: center;
        font-size: 18px; /* Adjusted font size */
        font-weight: bold;
        border-radius: 10px; /* Adjusted border radius */
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 5px 0; /* Adjusted margin */
        display: inline-block;
        text-decoration: none;
    }
    .gradient-button:hover {
        transform: scale(1.03); /* Adjusted scale */
        box-shadow: 0 4px 12px rgba(0,0,0,0.2); /* Adjusted shadow */
    }
    </style>
    <div class="top-right-gif">
        <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG1zM2JjZ3UyY25wcTdlZzc3aG16MWViZm12cGQ0M3JhZjZpeHFxOSZlcD12MV9pbnRlrm5hbF9naWZfYnlfaWQmY3Q9cw/aEWwGhZpWE7AGekRiZ/giphy.gif" width="230"> <!-- Updated URL and width -->
    </div>
    <div class="top-left-gif">
        <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MDUwdzV4dHFpeHg1NDJhZmk2bXc3Z2F0cW9zN3NxcXdlNmJweGFqcCZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q=cw/aEWwGhZpWE7AGekRiZ/giphy.gif" width="150"> <!-- Adjusted width -->
    </div>
    """, unsafe_allow_html=True
)

# -------------------------
# Homepage Title
# -------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:30px;">
        <h1 style="
            font-size: 45px;
            font-weight: bold;
            background: linear-gradient(to right, #ff7e5f, #feb47b, #86A8E7, #91EAE4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        ">🎬🍿 Welcome to IMDB Movies EDA</h1>
    </div>
    """, unsafe_allow_html=True
)

# Homepage GIF
st.markdown(
    """
    <div style="text-align:center; margin-bottom:30px;">
        <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cnE0a2M5Y2h2ZjAxOXp3enJxZjRyZDF2Y24yYjMyeW81b3U5NWYxcSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/JUwN8RdJAnSPsvy5eZ/giphy.gif" width="600">
    </div>
    """, unsafe_allow_html=True
)

# -------------------------
# Gradient Buttons with Callbacks - Now 4 buttons (removed chatbot button)
# -------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📄 Dataset Preview", use_container_width=True):
        st.session_state.section = "dataset"

with col2:
    if st.button("🔹 Basic Analysis", use_container_width=True):
        st.session_state.section = "basic"

with col3:
    if st.button("💰 Top Movies Analysis", use_container_width=True):
        st.session_state.section = "top_movies"

with col4:
    if st.button("🎯 Movie Recommendations", use_container_width=True):
        st.session_state.section = "recommendations"

# Apply CSS to buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    background: linear-gradient(90deg, #ff7e5f, #feb47b, #86A8E7, #91EAE4);
    color: white;
    font-size: 18px;
    font-weight: bold;
    height: 60px;
    border-radius: 15px;
    border: none;
}
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.markdown("## 🎛️ Filters")

# Genre filter
with st.sidebar.expander("🎬 Genre", expanded=True):
    genre_options = sorted(df['genre'].dropna().unique())
    st.session_state.genre_filter = st.multiselect("Select Genre", options=genre_options, default=st.session_state.genre_filter, key='genre_filter_widget')

# Certificate filter
with st.sidebar.expander("🎟️ Certificate", expanded=True):
    certificate_options = sorted(df['certificate'].dropna().astype(str).unique())
    st.session_state.certificate_filter = st.multiselect("Select Certificate", options=certificate_options, default=st.session_state.certificate_filter, key='certificate_filter_widget')

# Released Year filter
with st.sidebar.expander("📅 Released Year", expanded=True):
    year_min = int(df['released_year'].min(skipna=True)) if pd.notna(df['released_year'].min(skipna=True)) else 1900
    year_max = int(df['released_year'].max(skipna=True)) if pd.notna(df['released_year'].max(skipna=True)) else 2025
    st.session_state.year_filter = st.slider("Year Range", min_value=year_min, max_value=year_max,
                           value=st.session_state.year_filter, step=1, key='year_filter_widget')

# IMDB Rating filter
with st.sidebar.expander("⭐ IMDB Rating", expanded=True):
    rating_min = float(df['imdb_rating'].min(skipna=True)) if pd.notna(df['imdb_rating'].min(skipna=True)) else 0.0
    rating_max = float(df['imdb_rating'].max(skipna=True)) if pd.notna(df['imdb_rating'].max(skipna=True)) else 10.0
    st.session_state.rating_filter = (rating_min, rating_max)
    st.session_state.rating_filter = st.slider("Rating Range", min_value=rating_min, max_value=rating_max,
                           value=st.session_state.rating_filter, step=0.1, key='rating_filter_widget')

# Runtime filter
with st.sidebar.expander("⏱️ Runtime", expanded=True):
    runtime_min = int(df['runtime'].min(skipna=True)) if not pd.isna(df['runtime'].min(skipna=True)) else 0
    runtime_max = int(df['runtime'].max(skipna=True)) if not pd.isna(df['runtime'].max(skipna=True)) else 180
    st.session_state.runtime_filter = st.slider("Runtime (minutes)", min_value=runtime_min, max_value=runtime_max,
                           value=st.session_state.runtime_filter, step=5, key='runtime_filter_widget')

# Meta Score filter
if 'meta_score' in df.columns:
    with st.sidebar.expander("📊 Meta Score", expanded=True):
        meta_min = int(df['meta_score'].min(skipna=True)) if not pd.isna(df['meta_score'].min(skipna=True)) else 0
        meta_max = int(df['meta_score'].max(skipna=True)) if not pd.isna(df['meta_score'].max(skipna=True)) else 100
        st.session_state.meta_score_filter = st.slider("Meta Score Range", min_value=meta_min, max_value=meta_max,
                               value=st.session_state.meta_score_filter, step=1, key='meta_score_filter_widget')

# Actor filter
with st.sidebar.expander("🎭 Actors", expanded=True):
    all_actors = set()
    for col in ['star1', 'star2', 'star3', 'star4']:
        if col in df.columns:
            all_actors.update(df[col].dropna().unique())
    all_actors = sorted(all_actors)
    st.session_state.actor_filter = st.multiselect("Select Actors", options=all_actors, default=st.session_state.actor_filter, key='actor_filter_widget')


# Reset filters button at the bottom of filters
if st.sidebar.button("🔄 Reset All Filters", use_container_width=True):
    # Reset session state variables associated with filters
    st.session_state.genre_filter = []
    st.session_state.certificate_filter = []
    year_min = int(df['released_year'].min(skipna=True)) if pd.notna(df['released_year'].min(skipna=True)) else 1900
    year_max = int(df['released_year'].max(skipna=True)) if pd.notna(df['released_year'].max(skipna=True)) else 2025
    st.session_state.year_filter = (year_min, year_max) # Resetting to the default range
    rating_min = float(df['imdb_rating'].min(skipna=True)) if pd.notna(df['imdb_rating'].min(skipna=True)) else 0.0
    rating_max = float(df['imdb_rating'].max(skipna=True)) if pd.notna(df['imdb_rating'].max(skipna=True)) else 10.0
    st.session_state.rating_filter = (rating_min, rating_max) # Resetting to the default range
    runtime_min = int(df['runtime'].min(skipna=True)) if not pd.isna(df['runtime'].min(skipna=True)) else 0
    runtime_max = int(df['runtime'].max(skipna=True)) if not pd.isna(df['runtime'].max(skipna=True)) else 180
    st.session_state.runtime_filter = (runtime_min, runtime_max) # Resetting to the default range
    if 'meta_score' in df.columns:
         st.session_state.meta_score_filter = (int(df['meta_score'].min(skipna=True)) if not pd.isna(df['meta_score'].min(skipna=True)) else 0, int(df['meta_score'].max(skipna=True)) if not pd.isna(df['meta_score'].max(skipna=True)) else 100) # Resetting to default range
    st.session_state.actor_filter = []

    # Setting reset_filters to True is no longer strictly necessary if we rerun directly
    # st.session_state.reset_filters = True
    st.rerun()


# Apply Filters with more flexible logic
filtered_df = df.copy()

# Apply filters only if they are selected
if st.session_state.genre_filter:
    # Create a pattern to match any of the selected genres
    genre_pattern = '|'.join([re.escape(g) for g in st.session_state.genre_filter]) # Escape special characters
    filtered_df = filtered_df[filtered_df['genre'].str.contains(genre_pattern, na=False, case=False)]

if st.session_state.certificate_filter:
    filtered_df = filtered_df[filtered_df['certificate'].astype(str).isin(st.session_state.certificate_filter)]

# Apply range filters with NaN handling
filtered_df = filtered_df[
    (filtered_df['released_year'].isna() | ((filtered_df['released_year'] >= st.session_state.year_filter[0]) & (filtered_df['released_year'] <= st.session_state.year_filter[1]))) &
    (filtered_df['imdb_rating'].isna() | ((filtered_df['imdb_rating'] >= st.session_state.rating_filter[0]) & (filtered_df['imdb_rating'] <= st.session_state.rating_filter[1]))) &
    (filtered_df['runtime'].isna() | ((filtered_df['runtime'] >= st.session_state.runtime_filter[0]) & (filtered_df['runtime'] <= st.session_state.runtime_filter[1])))
]

# Apply meta score filter if available
if 'meta_score' in df.columns:
    filtered_df = filtered_df[
        (filtered_df['meta_score'].isna() | ((filtered_df['meta_score'] >= st.session_state.meta_score_filter[0]) & (filtered_df['meta_score'] <= st.session_state.meta_score_filter[1])))
    ]

# Apply actor filter if any actors are selected
if st.session_state.actor_filter:
    actor_filter_mask = filtered_df[['star1', 'star2', 'star3', 'star4']].apply(
        lambda row: any(actor in row.values for actor in st.session_state.actor_filter), axis=1
    )
    filtered_df = filtered_df[actor_filter_mask]

# -------------------------
# Display Sections
# -------------------------
if st.session_state.section == "dataset":
    st.subheader("📄 Dataset Preview")

    # Display basic dataset info with safe handling of NaN values
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Movies", len(filtered_df))
    with col2:
        st.metric("Columns", filtered_df.shape[1])
    with col3:
        # Safely calculate time span
        if not filtered_df.empty and pd.notna(filtered_df['released_year']).any():
            min_year = int(filtered_df['released_year'].min(skipna=True))
            max_year = int(filtered_df['released_year'].max(skipna=True))
            time_span = f"{min_year}-{max_year}"
        else:
            time_span = "N/A"
        st.metric("Time Span", time_span)

    # Show dataframe if not empty
    if not filtered_df.empty:
        st.dataframe(filtered_df.head(5))

        # Show posters preview
        st.markdown("### 🎬 Posters Preview")
        cols = st.columns(5)
        for idx, row in filtered_df.head(5).iterrows():
            col = cols[idx % 5]
            with col:
                st.markdown(f"**{row['series_title']}**")
                if pd.notna(row['poster_link']):
                    st.image(row['poster_link'], width=120)
                else:
                    st.write("No poster available")
    else:
        st.warning("No movies match your filters. Please adjust your filter criteria.")
        st.dataframe(df.head(5))

elif st.session_state.section == "basic":
    analysis_type = st.selectbox("Select Analysis Type:", ["Univariate Analysis", "Bivariate Analysis"])
    st.info(f"🔹 You selected: {analysis_type}")

    if analysis_type == "Univariate Analysis":
        st.subheader("📊 Univariate Analysis")

        # Numerical columns distribution with simplified histogram
        numerical_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()

        if numerical_cols:
            selected_num_col = st.selectbox("Select Numerical Column:", numerical_cols, key="num_col")
            
            # Create simple histogram with Plotly
            fig = px.histogram(
                filtered_df, 
                x=selected_num_col, 
                nbins=20,  # Fixed number of bins for simplicity
                title=f'Distribution of {selected_num_col.replace("_", " ").title()}',
                labels={selected_num_col: selected_num_col.replace("_", " ").title()},
                color_discrete_sequence=['#86A8E7']
            )
            
            fig.update_layout(
                height=500,
                showlegend=False,
                bargap=0.1  # Add some gap between bars for better visibility
            )
            st.plotly_chart(fig, use_container_width=True)
            
 
        st.markdown("---") # Add a separator

        # Categorical columns with larger layout
        categorical_cols = [col for col in filtered_df.select_dtypes(include='object').columns.tolist() 
                           if col not in ['poster_link', 'series_title', 'overview']]

        if categorical_cols:
            selected_cat_col = st.selectbox("Select Categorical Column:", categorical_cols, key="cat_col")

            # Get top 10 categories
            counts = filtered_df[selected_cat_col].value_counts().head(10)
            
            # Create horizontal bar chart with Plotly
            fig = px.bar(
                x=counts.values,
                y=counts.index,
                orientation='h',
                title=f'Top 10 {selected_cat_col.replace("_", " ").title()}',
                labels={'x': 'Count', 'y': selected_cat_col.replace("_", " ").title()},
                color=counts.values,
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=500,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No categorical columns available for analysis.")


    elif analysis_type == "Bivariate Analysis":
        st.subheader("📈 Bivariate Analysis")

        # Options for bivariate analysis
        bivariate_options = [
            "Gross by Certificate",
            "Gross by Genre",
            "Rating vs Gross",
            "Votes vs Gross",
            "Runtime vs Rating",
            "Meta Score vs Rating"
        ]
        selected_bivariate = st.selectbox("Select Analysis:", bivariate_options)

        if selected_bivariate == "Gross by Certificate" and 'gross' in filtered_df.columns and 'certificate' in filtered_df.columns:
            avg_gross = filtered_df.groupby('certificate')['gross'].mean().sort_values(ascending=True).tail(10)

            # Create horizontal bar chart with Plotly
            fig = px.bar(
                x=avg_gross.values,
                y=avg_gross.index,
                orientation='h',
                title='Average Gross by Certificate',
                labels={'x': 'Average Gross ($)', 'y': 'Certificate'},
                color=avg_gross.values,
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=500,
                xaxis_tickformat='$,.0f'
            )
            st.plotly_chart(fig, use_container_width=True)

        elif selected_bivariate == "Gross by Genre" and 'gross' in filtered_df.columns and 'genre' in filtered_df.columns:
            # Extract primary genre (first genre listed)
            filtered_df['primary_genre'] = filtered_df['genre'].str.split(',').str[0]
            avg_gross = filtered_df.groupby('primary_genre')['gross'].mean().sort_values(ascending=True).tail(10)

            # Create horizontal bar chart with Plotly
            fig = px.bar(
                x=avg_gross.values,
                y=avg_gross.index,
                orientation='h',
                title='Average Gross by Genre',
                labels={'x': 'Average Gross ($)', 'y': 'Genre'},
                color=avg_gross.values,
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=500,
                xaxis_tickformat='$,.0f'
            )
            st.plotly_chart(fig, use_container_width=True)

        elif selected_bivariate == "Rating vs Gross" and 'gross' in filtered_df.columns and 'imdb_rating' in filtered_df.columns:
            # Create scatter plot with Plotly
            fig = px.scatter(
                filtered_df,
                x='imdb_rating',
                y='gross',
                title='Rating vs Gross Revenue',
                labels={'imdb_rating': 'IMDB Rating', 'gross': 'Gross Revenue ($)'},
                trendline='ols'
            )
            fig.update_layout(
                height=500,
                yaxis_tickformat='$,.0f'
            )
            st.plotly_chart(fig, use_container_width=True)

        elif selected_bivariate == "Votes vs Gross" and 'gross' in filtered_df.columns and 'no_of_votes' in filtered_df.columns:
            # Create scatter plot with Plotly
            fig = px.scatter(
                filtered_df,
                x='no_of_votes',
                y='gross',
                title='Number of Votes vs Gross Revenue',
                labels={'no_of_votes': 'Number of Votes', 'gross': 'Gross Revenue ($)'},
                trendline='ols'
            )
            fig.update_layout(
                height=500,
                yaxis_tickformat='$,.0f'
            )
            st.plotly_chart(fig, use_container_width=True)

        elif selected_bivariate == "Runtime vs Rating" and 'runtime' in filtered_df.columns and 'imdb_rating' in filtered_df.columns:
            # Create scatter plot with Plotly
            fig = px.scatter(
                filtered_df,
                x='runtime',
                y='imdb_rating',
                title='Runtime vs Rating',
                labels={'runtime': 'Runtime (minutes)', 'imdb_rating': 'IMDB Rating'},
                trendline='ols'
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)

        elif selected_bivariate == "Meta Score vs Rating" and 'meta_score' in filtered_df.columns and 'imdb_rating' in filtered_df.columns:
            # Create scatter plot with Plotly
            fig = px.scatter(
                filtered_df,
                x='meta_score',
                y='imdb_rating',
                title='Meta Score vs Rating',
                labels={'meta_score': 'Meta Score', 'imdb_rating': 'IMDB Rating'},
                trendline='ols'
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("Required columns for this analysis are not available in the dataset.")


elif st.session_state.section == "top_movies":
    st.subheader("💰 Top Movies Analysis")

    # Add analysis type selection
    analysis_type = st.selectbox("Select Analysis Type:", ["Top/Bottom Movies by Gross", "Sequels vs Standalone"])

    if analysis_type == "Top/Bottom Movies by Gross" and 'gross' in filtered_df.columns:
        # Option to select top or bottom movies
        selection_type = st.radio("Select:", ["Top 5 Movies", "Bottom 5 Movies"])

        if selection_type == "Top 5 Movies":
            top_5 = filtered_df.nlargest(5, 'gross')[['series_title', 'gross', 'imdb_rating', 'released_year']]

            # Create horizontal bar chart with Plotly
            fig = px.bar(
                top_5,
                x='gross',
                y='series_title',
                orientation='h',
                title='Top 5 Movies by Gross Revenue',
                labels={'gross': 'Gross Revenue ($)', 'series_title': 'Movie Title'},
                color='gross',
                color_continuous_scale='Blues'
            )
            fig.update_layout(
                height=500,
                xaxis_tickformat='$,.0f',
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

            # Display data table
            st.write("### Top 5 Movies Details")
            display_df = top_5.copy()
            display_df['gross'] = display_df['gross'].apply(lambda x: f"${x:,.0f}")
            st.dataframe(display_df)

        else:  # Bottom 5 Movies
            bottom_5 = filtered_df.nsmallest(5, 'gross')[['series_title', 'gross', 'imdb_rating', 'released_year']]

            # Create horizontal bar chart with Plotly
            fig = px.bar(
                bottom_5,
                x='gross',
                y='series_title',
                orientation='h',
                title='Bottom 5 Movies by Gross Revenue',
                labels={'gross': 'Gross Revenue ($)', 'series_title': 'Movie Title'},
                color='gross',
                color_continuous_scale='Reds'
            )
            fig.update_layout(
                height=500,
                xaxis_tickformat='$,.0f',
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

            # Display data table
            st.write("### Bottom 5 Movies Details")
            display_df = bottom_5.copy()
            display_df['gross'] = display_df['gross'].apply(lambda x: f"${x:,.0f}")
            st.dataframe(display_df)

    elif analysis_type == "Sequels vs Standalone":
        st.subheader("🎬 Sequels vs Standalone Movies Analysis")

        if 'gross' in filtered_df.columns and 'is_sequel' in filtered_df.columns:
            # Comparison of average gross
            sequel_comparison = filtered_df.groupby('is_sequel')['gross'].mean().reset_index()
            sequel_comparison['is_sequel'] = sequel_comparison['is_sequel'].map({True: "Sequels", False: "Standalone"})

            # Create two columns for the charts
            col1, col2 = st.columns(2)

            with col1:
                # Create bar chart with Plotly
                fig = px.bar(
                    sequel_comparison,
                    x='is_sequel',
                    y='gross',
                    title='Average Gross by Movie Type',
                    labels={'is_sequel': 'Movie Type', 'gross': 'Average Gross ($)'},
                    color='is_sequel',
                    color_discrete_map={"Sequels": "#ff7e5f", "Standalone": "#86A8E7"}
                )
                fig.update_layout(
                    height=400,
                    yaxis_tickformat='$,.0f',
                    showlegend=False
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Percentage of sequels vs standalone
                sequel_count = filtered_df['is_sequel'].value_counts()
                
                # Create pie chart with Plotly
                fig = px.pie(
                    values=sequel_count.values,
                    names=['Standalone', 'Sequels'],
                    title='Percentage of Sequels vs Standalone Movies',
                    color=['Standalone', 'Sequels'],
                    color_discrete_map={"Standalone": "#86A8E7", "Sequels": "#ff7e5f"}
                )
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)

            # Top 5 sequels by gross
            st.write("### Top 5 Sequels by Gross Revenue")
            top_sequels = filtered_df[filtered_df['is_sequel']].nlargest(5, 'gross')[['series_title', 'gross', 'imdb_rating', 'released_year', 'star1', 'star2', 'star3', 'star4']]

            # Format the gross values for display
            display_df = top_sequels.copy()
            display_df['gross'] = display_df['gross'].apply(lambda x: f"${x:,.0f}")
            st.dataframe(display_df)
        else:
            st.warning("Required columns (gross or is_sequel) are not available for this analysis.")

elif st.session_state.section == "recommendations":
    st.subheader("🎯 Personalized Movie Recommendations")

    # Recommendation filters
    st.write("### Select your preferences:")

    col1, col2 = st.columns(2)
    with col1:
        selected_genre = st.selectbox("Genre Group:", options=sorted(filtered_df['genre_group'].unique()))
        selected_certificate = st.selectbox("Certificate Group:", options=sorted(filtered_df['certificate_group'].unique()))

    with col2:
        selected_year = st.selectbox("Era:", options=sorted(filtered_df['year_group'].unique()))
        # Removed actor selection from here

    # Filter movies based on preferences
    recommended_movies = filtered_df[
        (filtered_df['genre_group'] == selected_genre) &
        (filtered_df['certificate_group'] == selected_certificate) &
        (filtered_df['year_group'] == selected_year)
    ]

    # Apply actor filter from the sidebar
    if st.session_state.actor_filter:
        actor_filter_mask = recommended_movies[['star1', 'star2', 'star3', 'star4']].apply(
            lambda row: any(actor in row.values for actor in st.session_state.actor_filter), axis=1
        )
        recommended_movies = recommended_movies[actor_filter_mask]


    # Sort by rating and gross if available
    sort_columns = []
    if 'imdb_rating' in recommended_movies.columns:
        sort_columns.append('imdb_rating')
    if 'gross' in recommended_movies.columns:
        sort_columns.append('gross')

    if sort_columns:
        recommended_movies = recommended_movies.sort_values(sort_columns, ascending=[False, False])

    if not recommended_movies.empty:
        st.write(f"### 🎬 Top {min(5, len(recommended_movies))} Recommendations for You")

        # Display top recommendations
        for idx, row in recommended_movies.head(5).iterrows():
            with st.expander(f"{row['series_title']} ({row['released_year']}) - ⭐ {row['imdb_rating'] if 'imdb_rating' in row else 'N/A'}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    if pd.notna(row['poster_link']):
                        st.image(row['poster_link'], width=200)
                    else:
                        st.write("No poster available")

                with col2:
                    st.write(f"**Genre:** {row['genre']}")
                    st.write(f"**Certificate:** {row['certificate']}")
                    # Removed runtime display as requested
                    st.write(f"**Director:** {row['director']}")
                    stars = ", ".join([row[col] for col in ['star1', 'star2', 'star3', 'star4'] if col in row and pd.notna(row[col])])
                    st.write(f"**Stars:** {stars}")
                    if 'gross' in row:
                        st.write(f"**Gross Revenue:** ${row['gross']:,.0f}")
                    if 'overview' in row:
                        st.write(f"**Overview:** {row['overview']}")
    else:
        st.warning("No movies match your criteria. Try adjusting your filters.")

    # Display some statistics
    st.write("### 📊 Recommendation Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Matching Movies", len(recommended_movies))
    with col2:
        if 'imdb_rating' in recommended_movies.columns:
            avg_rating = recommended_movies['imdb_rating'].mean() if not recommended_movies.empty else 0
            st.metric("Average Rating", f"{avg_rating:.1f}")
        else:
            st.metric("Average Rating", "N/A")
    with col3:
        if 'gross' in recommended_movies.columns:
            avg_gross = recommended_movies['gross'].mean() if not recommended_movies.empty else 0
            st.metric("Average Gross", f"${avg_gross:,.0f}")
        else:
            st.metric("Average Gross", "N/A")