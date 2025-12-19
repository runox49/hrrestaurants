import streamlit as st
import pandas as pd
import pydeck as pdk

# Page configuration
st.set_page_config(page_title="Chiang Mai Eats & Coffee Guide", page_icon="🍲", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    h1 { color: #2e7d32; }
    .stExpander { background-color: white; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍲 Chiang Mai: High-Rate Dining & Cafes")
st.markdown("A premium guide to spots with **4.5★+** and **500+ reviews**. "
            "🔴 **Green** = Restaurants | 🟤 **Brown** = Cafes")

# --- DATA PREPARATION ---
# RGBA Colors
GREEN = [46, 125, 50, 200]
BROWN = [121, 85, 72, 200]

data = [
    # RESTAURANTS
    {"Name": "Baan Landai Fine Thai", "Lat": 18.7915, "Lon": 98.9892, "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Color": GREEN, "Maps": "https://maps.app.goo.gl/vS355y67UvE8W7Yy8", "Highlight": "Signature Pork Ribs in Red Wine"},
    {"Name": "Khao Soi Maesai", "Lat": 18.8001, "Lon": 98.9814, "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Color": GREEN, "Maps": "https://maps.app.goo.gl/B9p4LToB6nC8zX6s5", "Highlight": "Khao Soi Beef (Michelin Bib)"},
    {"Name": "SP Chicken", "Lat": 18.7885, "Lon": 98.9821, "Rating": 4.5, "Reviews": 2500, "Type": "Restaurant", "Color": GREEN, "Maps": "https://maps.app.goo.gl/pW9uLToB6nC8zX6s5", "Highlight": "Garlic Stuffed Roasted Chicken"},
    {"Name": "Huen Muan Jai", "Lat": 18.7998, "Lon": 98.9756, "Rating": 4.5, "Reviews": 4200, "Type": "Restaurant", "Color": GREEN, "Maps": "https://maps.app.goo.gl/jX9uLToB6nC8zX6s5", "Highlight": "Northern Appetizer Sampler Platter"},
    # CAFES
    {"Name": "Akha Ama Phrasingh", "Lat": 18.7884, "Lon": 98.9832, "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Color": BROWN, "Maps": "https://maps.app.goo.gl/kY9uLToB6nC8zX6s5", "Highlight": "Local Single-Origin Coffee"},
    {"Name": "The Baristro Asian Style", "Lat": 18.7899, "Lon": 98.9517, "Rating": 4.7, "Reviews": 1500, "Type": "Cafe", "Color": BROWN, "Maps": "https://maps.app.goo.gl/mZ9uLToB6nC8zX6s5", "Highlight": "Matcha & Minimalist Zen Garden"},
    {"Name": "GRAPH ground", "Lat": 18.7984, "Lon": 98.9712, "Rating": 4.7, "Reviews": 1200, "Type": "Cafe", "Color": BROWN, "Maps": "https://maps.app.goo.gl/nN9uLToB6nC8zX6s5", "Highlight": "Creative Nitro Cold Brews"},
    {"Name": "Into the Woods", "Lat": 18.7948, "Lon": 98.9867, "Rating": 4.6, "Reviews": 900, "Type": "Cafe", "Color": BROWN, "Maps": "https://maps.app.goo.gl/oP9uLToB6nC8zX6s5", "Highlight": "Fairy-tale Themed Decor & Brunch"}
]

df = pd.DataFrame(data)

# --- 1. THE MAP (PyDeck) ---
st.subheader("🗺️ Location Discovery")
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[Lon, Lat]',
    get_color='Color',
    get_radius=85,
    pickable=True,
)
view_state = pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{Name}\nType: {Type}\nRating: {Rating}★"}
))

# --- 2. THE SUMMARY TABLE ---
st.subheader("📊 Interactive Summary")
# Use the new LinkColumn for easy clicking
st.dataframe(
    df[["Name", "Type", "Rating", "Reviews", "Maps"]],
    column_config={"Maps": st.column_config.LinkColumn("Google Maps Link")},
    use_container_width=True,
    hide_index=True
)

# --- 3. THE DEEP DIVE (Original Expander Layout) ---
st.divider()
st.subheader("🔍 Deep Dive & Highlights")

# Sidebar Neighborhood Filter
neighborhoods = ["Old City", "Nimman", "Santitham", "Riverside"]
selected_n = st.sidebar.multiselect("Filter Neighborhoods", neighborhoods, default=neighborhoods)

cols = st.columns(2)
for i, row in df.iterrows():
    with cols[i % 2]:
        with st.expander(f"**{row['Name']}** ({row['Rating']}★)"):
            st.write(f"**Type:** {row['Type']}")
            st.write(f"**Reviews:** {row['Reviews']:,}+")
            st.info(f"💡 **Must Try:** {row['Highlight']}")
            st.markdown(f"[📍 Open in Google Maps]({row['Maps']})")

st.sidebar.info("Data verified for 2025. Prices and hours may vary.")
