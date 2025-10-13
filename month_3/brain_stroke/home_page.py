import streamlit as st

def show_home_page():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="sub-header">🚨 WHAT IS A BRAIN STROKE?</div>', unsafe_allow_html=True)
        st.markdown("""
        A stroke occurs when blood flow to the brain is interrupted or reduced. 
        This prevents brain tissue from getting oxygen and nutrients, causing brain cells to die within minutes.
        
        ### ⚡ URGENT FACTS:
        - Every 40 seconds, someone has a stroke
        - Every 3.5 minutes, someone dies of stroke
        - Stroke is the #5 cause of death in the US
        """)
        
        # FAST Protocol
        st.markdown('<div class="sub-header">🆘 STROKE RECOGNITION - F.A.S.T.</div>', unsafe_allow_html=True)
        
        fast_cols = st.columns(4)
        with fast_cols[0]:
            st.markdown('<div class="metric-card"><h3>🧬 FACE</h3>Ask person to smile</div>', unsafe_allow_html=True)
        with fast_cols[1]:
            st.markdown('<div class="metric-card"><h3>💪 ARMS</h3>Ask to raise both arms</div>', unsafe_allow_html=True)
        with fast_cols[2]:
            st.markdown('<div class="metric-card"><h3>🗣️ SPEECH</h3>Ask to repeat a phrase</div>', unsafe_allow_html=True)
        with fast_cols[3]:
            st.markdown('<div class="metric-card"><h3>⏰ TIME</h3>CALL 911 IMMEDIATELY!</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="sub-header">📞 EMERGENCY RESPONSE</div>', unsafe_allow_html=True)
        st.markdown("""
        **🚑 CALL 911 IMMEDIATELY**
        
        **DO NOT:**
        ❌ Drive yourself to hospital
        ❌ Wait to see if symptoms go away
        ❌ Give aspirin
        """)
        
        # Risk factors
        st.markdown('<div class="sub-header">🎯 RISK FACTORS</div>', unsafe_allow_html=True)
        risk_factors = [
            "🔴 High Blood Pressure",
            "🔴 Diabetes",
            "🔴 Smoking",
            "🔴 Obesity",
            "🔴 Heart Disease",
            "🔴 High Cholesterol"
        ]
        
        for factor in risk_factors:
            st.markdown(f'{factor}')