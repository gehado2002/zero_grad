# airline_app_plotly_gradient.py
import streamlit as st
import pandas as pd
import plotly.express as px
from textwrap import dedent

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Flying Happy — Airline Passenger Satisfaction",
    page_icon="✈️",
    layout="wide"
)

# -------------------------
# Sidebar Gradient CSS
# -------------------------
st.markdown(
    """
    <style>
    /* Sidebar gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, black, white);
        color: white;
    }
    /* Sidebar text color */
    [data-testid="stSidebar"] .css-1d391kg p, 
    [data-testid="stSidebar"] .css-1d391kg label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Home Page Title & Image
# -------------------------
st.markdown('<div style="text-align:center; font-size:32px; font-weight:700">✈️ Flying Happy Dashboard</div>', unsafe_allow_html=True)
st.image("https://www.elliott.org/wp-content/uploads/No-Room.png")
st.markdown('<div style="text-align:center; font-size:18px;">Select a section to explore</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "📊 **Data Source:** [Kaggle - Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction) ",
    unsafe_allow_html=True
)
st.markdown(
    "💻 **Full Data Analysis Project:** [Open in Colab](https://colab.research.google.com/drive/1cthJ5HJ27cRsUYUx5AN61JP7EOFOG17Y)",
    unsafe_allow_html=True
)

# -------------------------
# Helpers: load & normalize
# -------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower().str.replace(" ", "_").str.strip()
    return df

def pick_col(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

# -------------------------
# Load dataset
# -------------------------
st.sidebar.header("Load data & Filters")
csv_path = "airline_passenger_satisfaction.csv"

if not csv_path:
    st.sidebar.error("Please provide CSV path")

try:
    df = load_data(csv_path)
except Exception as e:
    st.warning("Provide valid CSV path.")
    st.stop()

# -------------------------
# Detect columns
# -------------------------
col_mapping = {
    "satisfaction": ["satisfaction"],
    "class": ["class", "cabin_class"],
    "customer_type": ["customer type", "customer_type"],
    "type_of_travel": ["type_of_travel", "type of travel"],
    "gender": ["gender"],
    "age": ["age"],
    "departure_delay": ["departure_delay", "departure delay"],
    "arrival_delay": ["arrival_delay", "arrival delay"]
}

col_satisfaction = pick_col(df, col_mapping["satisfaction"])
col_class = pick_col(df, col_mapping["class"])
col_customer_type = pick_col(df, col_mapping["customer_type"])
col_travel_type = pick_col(df, col_mapping["type_of_travel"])
col_gender = pick_col(df, col_mapping["gender"])
col_age = pick_col(df, col_mapping["age"])
col_dep_delay = pick_col(df, col_mapping["departure_delay"])
col_arr_delay = pick_col(df, col_mapping["arrival_delay"])

# -------------------------
# Sidebar filters
# -------------------------
st.sidebar.markdown("### Filters")
sel_class = st.sidebar.selectbox(
    "Class",
    ["All"] + sorted(df[col_class].dropna().unique().tolist())
) if col_class else "All"

sel_cust = st.sidebar.selectbox(
    "Customer Type",
    ["All"] + sorted(df[col_customer_type].dropna().unique().tolist())
) if col_customer_type else "All"

sel_travel = st.sidebar.selectbox(
    "Type of Travel",
    ["All"] + sorted(df[col_travel_type].dropna().unique().tolist())
) if col_travel_type else "All"

sel_gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df[col_gender].dropna().unique().tolist())
) if col_gender else "All"

sel_age = st.sidebar.slider(
    "Age range",
    int(df[col_age].min()), int(df[col_age].max()),
    (int(df[col_age].min()), int(df[col_age].max()))
) if col_age else None

# Apply filters
df_filtered = df.copy()
if sel_class != "All": df_filtered = df_filtered[df_filtered[col_class] == sel_class]
if sel_cust != "All": df_filtered = df_filtered[df_filtered[col_customer_type] == sel_cust]
if sel_travel != "All": df_filtered = df_filtered[df_filtered[col_travel_type] == sel_travel]
if sel_gender != "All": df_filtered = df_filtered[df_filtered[col_gender] == sel_gender]
if sel_age: df_filtered = df_filtered[(df_filtered[col_age] >= sel_age[0]) & (df_filtered[col_age] <= sel_age[1])]

# -------------------------
# Overview Section
# -------------------------
def overview_section(df):
    st.subheader("Overview & Demographics")
    st.markdown(f"Filtered rows: {len(df):,}")

    # Pie chart
    fig = px.pie(df, names=col_satisfaction, color=col_satisfaction, 
                 color_discrete_map={df[col_satisfaction].unique()[0]:"#5C4033",
                                     df[col_satisfaction].unique()[1]:"blue"},
                 title="Overall Satisfaction Distribution")
    st.plotly_chart(fig, use_container_width=True)
    
    # Age group
    if col_age:
        bins = [0, 24, 39, 54, 100]
        labels = ["<25", "25-39", "40-54", "55+"]
        df["age_group"] = pd.cut(df[col_age], bins=bins, labels=labels, include_lowest=True)

    # Line chart comparison
    available_cols = [col_class, col_customer_type, col_gender]
    if col_age: available_cols.append("age_group")
    chosen_col = st.selectbox("Compare with Satisfaction:", available_cols)

    service_columns = [
        'check-in_service', 'online_boarding', 'gate_location',
        'on-board_service', 'seat_comfort', 'leg_room_service', 'cleanliness',
        'food_and_drink', 'in-flight_service', 'in-flight_wifi_service',
        'in-flight_entertainment', 'baggage_handling'
    ]

    df_plot = df[service_columns + [chosen_col]].copy()
    df_plot = df_plot.melt(id_vars=[chosen_col], value_vars=service_columns, var_name="Service", value_name="Rating")
    df_plot = df_plot[df_plot["Rating"] >= 4]
    df_plot_grouped = df_plot.groupby([chosen_col, "Service"]).size().reset_index(name="Satisfied Count")
    
    total_counts = df.groupby(chosen_col).size().to_dict()
    df_plot_grouped["Percentage Satisfied"] = df_plot_grouped.apply(lambda row: row["Satisfied Count"]/total_counts[row[chosen_col]]*100, axis=1)

    fig = px.line(df_plot_grouped, x="Service", y="Percentage Satisfied", color=chosen_col, markers=True,
                  title=f'Passenger Satisfaction by {chosen_col.replace("_"," ").title()}')
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Service Ratings Section
# -------------------------
def service_section(df):
    st.subheader("Service Impact")
    services = ["departure_and_arrival_time_convenience", "on-board_service", "seat_comfort","leg_room_service",
                "cleanliness","food_and_drink","in-flight_service","in-flight_wifi_service",
                "in-flight_entertainment","baggage_handling"]
    services_present = [s for s in services if s in df.columns]
    if not services_present: 
        st.warning("No service columns found in this dataset.")
        return

    # ------------------------- Heatmap -------------------------
    df_num = df[services_present].apply(pd.to_numeric, errors='coerce').dropna()
    fig_heatmap = px.imshow(df_num.corr(), text_auto=".2f", aspect="auto",
                            title="Correlation Heatmap of Service Ratings")
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # ------------------------- Highlight Most Impactful Services -------------------------
    if col_satisfaction:
        satisfied_df = df[df[col_satisfaction].str.lower() == 'satisfied']
        high_rating_counts = {col: satisfied_df[satisfied_df[col] >= 4][col].count()
                              for col in services_present}
        high_rating_df = pd.DataFrame(list(high_rating_counts.items()),
                                      columns=['Service', 'Count of Satisfied (Rating >= 4)'])
        high_rating_df = high_rating_df.sort_values(by='Count of Satisfied (Rating >= 4)', ascending=False)
        
        st.markdown("**Services Most Strongly Driving Satisfaction**")
        fig_bar = px.bar(high_rating_df, x='Service', y='Count of Satisfied (Rating >= 4)',
                         title='Number of Satisfied Passengers with High Ratings (4 or 5) for Each Service')
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------
# Flight Operations Section
# -------------------------
def operations_section(df):
    st.subheader("Flight Operations & Conclusions")
    delay_options = []
    if col_dep_delay: delay_options.append("Departure Delay")
    if col_arr_delay: delay_options.append("Arrival Delay")

    if delay_options:
        delay_type = st.radio("Choose Delay Type:", delay_options, horizontal=True)
        col_name = col_dep_delay if delay_type=="Departure Delay" else col_arr_delay
        fig = px.box(df, x=col_satisfaction, y=col_name, color=col_satisfaction,
                     title=f"{delay_type} by Satisfaction", color_discrete_map={df[col_satisfaction].unique()[0]:"#1f77b4",
                                                                               df[col_satisfaction].unique()[1]:"#d62728"})
        st.plotly_chart(fig, use_container_width=True)

    if col_travel_type:
        fig = px.histogram(df, x=col_travel_type, color=col_satisfaction, barmode="group",
                           title=f"{col_travel_type.replace('_',' ').title()} vs {col_satisfaction.title()}")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Conclusions & Recommendations:**")
    st.markdown(dedent("""
        - Improve services with weak correlation to satisfaction.
        - Focus on premium classes and loyal customers.
        - Reduce departure/arrival delays to increase satisfaction.
        - Target demographic segments with lower satisfaction.
    """))

# -------------------------
# Display section
# -------------------------
section_to_show = st.radio(
    "Dashboard Sections:",
    ["Overview", "Service Ratings", "Flight Operations"],
    index=0,
    horizontal=True
)

if section_to_show == "Overview":
    overview_section(df_filtered)
elif section_to_show == "Service Ratings":
    service_section(df_filtered)
elif section_to_show == "Flight Operations":
    operations_section(df_filtered)
