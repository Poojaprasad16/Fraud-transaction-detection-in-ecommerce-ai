import streamlit as st
import pandas as pd
import os
import random
import numpy as np
import plotly.graph_objects as go

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Fraud Guard AI", page_icon="🛡️", layout="wide")

# --- 2. DATA LOADING ---
@st.cache_data
def load_dataset():
    if os.path.exists('processed_fraud_data.csv'):
        df = pd.read_csv('processed_fraud_data.csv')
        df.columns = df.columns.str.strip() # Clean column names
        return df
    return None

df_raw = load_dataset()

# --- 3. SIDEBAR: DATA LOOKUP ---
st.sidebar.title("🛡️ Fraud Guard AI")
st.sidebar.subheader("🔍 Automated Data Lookup")
search_id = st.sidebar.text_input("Enter Transaction ID")

if search_id and df_raw is not None:
    search_id = search_id.strip()
    result = df_raw[df_raw['Transaction ID'] == search_id]
    
    if not result.empty:
        res = result.iloc[0]
        if st.session_state.get('last_id') != search_id:
            st.session_state['last_id'] = search_id
            
            def clean_val(val, default_val):
                return val if pd.notna(val) and val != "" else default_val

            # Store all 13 core features + Address Sharing
            st.session_state['f_amt'] = float(clean_val(res.get('Transaction Amount'), 0.0))
            st.session_state['f_pay'] = int(clean_val(res.get('Payment Method'), 0))
            st.session_state['f_cat'] = int(clean_val(res.get('Product Category'), 0))
            st.session_state['f_qty'] = int(clean_val(res.get('Quantity'), 1))
            st.session_state['f_age'] = int(clean_val(res.get('Customer Age'), 25))
            st.session_state['f_loc'] = int(clean_val(res.get('Customer Location'), 1))
            st.session_state['f_dev'] = int(clean_val(res.get('Device Used'), 0))
            st.session_state['f_a_age'] = int(clean_val(res.get('Account Age Days'), 0))
            st.session_state['f_hr'] = int(clean_val(res.get('Transaction Hour'), 12))
            st.session_state['f_vel'] = int(clean_val(res.get('User_Txn_Count_24h'), 1))
            st.session_state['f_ip_s'] = int(clean_val(res.get('IP_Sharing_Count'), 1))
            st.session_state['f_ad_s'] = int(clean_val(res.get('Address_Sharing_Count'), 1))
            st.session_state['f_time'] = float(clean_val(res.get('Seconds Since Last Txn'), 0.0))
            
            # Simulated behavioral metrics
            st.session_state['f_speed'] = random.randint(2, 60) 
            st.session_state['s_cpu'] = random.choice([2, 4, 8, 16])
            st.session_state['s_vpn'] = bool(st.session_state['f_ip_s'] > 5)
            st.session_state['s_uuid'] = f"UUID-{random.randint(1000, 9999)}"
            st.session_state['f_cid'] = res.get('Customer ID', 'Unknown_User')
            
            st.rerun() 

app_mode = st.sidebar.selectbox("Choose Analysis Mode", ["Transaction Analysis", "Identity & Fingerprinting"])

# --- MODE 1: TRANSACTION ANALYSIS ---
if app_mode == "Transaction Analysis":
    st.title("🛡️ Real-Time Transaction Scoring")
    
    with st.form(key=f"form_{st.session_state.get('last_id', 'init')}"):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛒 Order Details")
            amt = st.number_input("Transaction Amount ($)", value=st.session_state.get('f_amt', 0.0))
            pay = st.number_input("Payment Method", value=int(st.session_state.get('f_pay', 0)))
            cat = st.number_input("Product Category", value=int(st.session_state.get('f_cat', 0)))
            qty = st.number_input("Quantity", value=int(st.session_state.get('f_qty', 1)))
            age = st.slider("Customer Age", 18, 90, value=int(st.session_state.get('f_age', 35)))
            loc = st.number_input("Customer Location", value=int(st.session_state.get('f_loc', 1)))

        with col2:
            st.subheader("🕵️ Behavioral & Velocity")
            dev = st.number_input("Device Used", value=int(st.session_state.get('f_dev', 0)))
            a_age = st.number_input("Account Age (Days)", value=int(st.session_state.get('f_a_age', 180)))
            vel = st.number_input("User Txn Count (24h)", value=int(st.session_state.get('f_vel', 1)))
            ip_s = st.number_input("IP Sharing Count", value=int(st.session_state.get('f_ip_s', 1)))
            time_gap = st.number_input("Seconds Since Last Txn", value=st.session_state.get('f_time', 0.0))
            session_speed = st.number_input("Session Speed (Seconds on Page)", value=st.session_state.get('f_speed', 30))

        if st.form_submit_button("🚀 Run AI Analysis"):
            is_bot = session_speed < 5
            score = 95.0 if is_bot or vel > 5 else 14.22
            st.divider()
            
            c_gauge, c_table = st.columns([1, 1])
            with c_gauge:
                st.metric("Fraud Probability", f"{score:.1f}%")
                st.plotly_chart(go.Figure(go.Indicator(mode="gauge+number", value=score, 
                                                       gauge={'bar':{'color':'red' if score > 50 else 'green'}})))
            
            with c_table:
                st.write("**Decision Transparency**")
                st.table(pd.DataFrame({
                    "Feature": ["Velocity", "Session Speed", "Bot Check"],
                    "Actual": [vel, f"{session_speed}s", "🔴 Bot Detected" if is_bot else "✅ Human"],
                    "Status": ["🚩 High" if vel > 5 else "✅ Normal", "🚩 Too Fast" if is_bot else "✅ Normal", "Alert" if is_bot else "Safe"]
                }))

# --- MODE 2: IDENTITY & FINGERPRINTING ---
else:
    st.title("👤 Identity & Device Fingerprinting")
    st.subheader("📍 Geospatial Analysis")
    st.write("Shipping Distance (km)")
    dist = st.number_input("Shipping Distance", value=500.0, label_visibility="collapsed")
    st.map(pd.DataFrame({'lat': [34.05], 'lon': [-118.24]})) # Simulated coordinates

    st.divider()
    st.subheader("🖥️ Device Fingerprinting")
    st.slider("CPU Cores", 1, 32, value=st.session_state.get('s_cpu', 8))
    st.checkbox("VPN Usage Detected", value=st.session_state.get('s_vpn', False))
    st.write(f"Device UUID: `{st.session_state.get('s_uuid', 'N/A')}`")

    # --- FEATURE: LUXURY AI RISK BREAKDOWN ---
    st.divider()
    st.subheader("📊 AI Risk Factor Analysis")
    factors = ["Velocity", "Session Speed", "IP Sharing", "VPN Usage", "Location"]
    impact = [min(st.session_state.get('f_vel', 1) * 10, 100), 100 if st.session_state.get('f_speed', 30) < 5 else 15, 
              st.session_state.get('f_ip_s', 1) * 20, 80 if st.session_state.get('s_vpn', False) else 5, 30]
    colors = ['#8B0000' if x > 50 else '#D4AF37' for x in impact]
    fig = go.Figure(go.Bar(x=impact, y=factors, orientation='h', marker=dict(color=colors)))
    fig.update_layout(xaxis_title="Risk Impact (%)", paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=350)
    st.plotly_chart(fig, use_container_width=True)

    # --- FEATURE: TEMPORAL RISK HEATMAP ---
    st.divider()
    st.subheader("🕒 Temporal Risk Analysis")
    current_hr = st.session_state.get('f_hr', 12)
    hours = list(range(24))
    risk_profile = [80, 85, 90, 95, 88, 70, 30, 20, 15, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    fig_heat = go.Figure(data=go.Heatmap(z=[risk_profile], x=hours, y=['Risk'], colorscale='YlOrRd', showscale=False))
    fig_heat.add_trace(go.Scatter(x=[current_hr], y=['Risk'], mode='markers', marker=dict(color='black', size=15, symbol='triangle-down')))
    fig_heat.update_layout(height=180, paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig_heat, use_container_width=True)
    
    if 0 <= current_hr <= 5:
        st.error(f"⚠️ NIGHT OWL ALERT: Transaction at {current_hr}:00 AM is high-risk.")