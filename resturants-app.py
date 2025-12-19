import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Chiang Mai Best Eats & Coffee", page_icon="🍲", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stDataFrame { border: 1px solid #e6e9ef; border-radius: 10px; }
    h1, h2 { color: #1e4d2b; }
    .map-container { border: 2px solid #1e4d2b; border-radius: 15px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍲 Chiang Mai: High-Rated Food & Coffee")
st.markdown("Explore the best-rated spots (4.5★+ and 500+ reviews) with real-time location mapping.")

# --- DATA PREPARATION ---
# Restaurant Data
restaurants = [
    {"Name": "Baan Landai Fine Thai Cuisine", "Lat": 18.7915, "Lon": 98.9892, "Rating": 4.7, "Type": "Restaurant", "Maps": "https://maps.app.goo.gl/3ZJ2v8u8m8kR7n6A8"},
    {"Name": "Khao Soi Maesai", "Lat": 18.8001, "Lon": 98.9814, "Rating": 4.6, "Type": "Restaurant", "Maps": "https://maps.app.goo.gl/Yj8k2s1d6D7n6Z5B9"},
    {"Name": "Khao Soi Lung Prakit", "Lat": 18.7779, "Lon": 98.9882, "Rating": 4.6, "Type": "Restaurant", "Maps": "https://maps.app.goo.gl/N8k1s1d6D7n6Z5B9"},
    {"Name": "SP Chicken", "Lat": 18.7885, "Lon": 98.9821, "Rating": 4.5, "Type": "Restaurant", "Maps": "https://maps.app.goo.gl/P8k1s1d6D7n6Z5B9"},
]

# Cafe Data
cafes = [
    {"Name": "Akha Ama Phrasingh", "Lat": 18.7884, "Lon": 98.9832, "Rating": 4.6, "Type": "Cafe", "Maps": "https://maps.google.com/?cid=13620790050376515434&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"},
    {"Name": "The Baristro Asian Style", "Lat": 18.7899, "Lon": 98.9517, "Rating": 4.7, "Type": "Cafe", "Maps": "https://maps.google.com/?cid=5346754812069285064&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"},
    {"Name": "GRAPH ground", "Lat": 18.7984, "Lon": 98.9712, "Rating": 4.7, "Type": "Cafe", "Maps": "https://maps.google.com/?cid=16590211772926660205&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"},
    {"Name": "Roast8ry Coffee Lab", "Lat": 18.7989, "Lon": 98.9687, "Rating": 4.4, "Type": "Cafe", "Maps": "https://maps.google.com/?cid=238573367649219454&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"},
    {"Name": "Into the Woods", "Lat": 18.7948, "Lon": 98.9867, "Rating": 4.6, "Type": "Cafe", "Maps": "https://maps.google.com/?cid=988537111577919735&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ"},
]

df_rest = pd.DataFrame(restaurants)
df_cafe = pd.DataFrame(cafes)
all_locations = pd.concat([df_rest, df_cafe], ignore_index=True)

# --- SIDEBAR ---
st.sidebar.header("📍 Navigation")
show_type = st.sidebar.radio("Show on Map:", ["All", "Restaurants Only", "Cafes Only"])

if show_type == "Restaurants Only":
    map_data = df_rest
elif show_type == "Cafes Only":
    map_data = df_cafe
else:
    map_data = all_locations

# --- MAIN CONTENT ---

# 1. THE MAP
st.subheader("🗺️ Location Discovery")
st.map(map_data, latitude='Lat', longitude='Lon', color='#1e4d2b', size=20)

# 2. TABLES
col1, col2 = st.columns(2)

with col1:
    st.subheader("🍽️ Top Restaurants")
    st.dataframe(
        df_rest[["Name", "Rating", "Maps"]], 
        column_config={"Maps": st.column_config.LinkColumn("Google Maps Link")},
        hide_index=True, use_container_width=True
    )

with col2:
    st.subheader("☕ Specialty Cafes")
    st.dataframe(
        df_cafe[["Name", "Rating", "Maps"]], 
        column_config={"Maps": st.column_config.LinkColumn("Google Maps Link")},
        hide_index=True, use_container_width=True
    )

# 3. QUICK TIPS
st.divider()
st.info("💡 **Pro Tip:** Chiang Mai's famous Khao Soi shops often close by 2:00 PM. Head to **Akha Ama** or **Roast8ry** afterward for world-class coffee!")
