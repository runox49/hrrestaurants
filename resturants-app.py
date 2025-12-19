import streamlit as st
import pandas as pd
import pydeck as pdk

# Page configuration
st.set_page_config(page_title="Chiang Mai Food & Coffee Map", page_icon="📍", layout="wide")

st.title("🍲 Chiang Mai High-Rate Guide")
st.markdown("Green dots = **Restaurants** | Brown dots = **Cafes** (4.5★+ and 500+ reviews)")

# --- DATA PREPARATION ---
# Color codes in [R, G, B, Alpha]
GREEN = [46, 125, 50, 200]  # Restaurant Green
BROWN = [121, 85, 72, 200]  # Cafe Brown

data = [
    # Restaurants
    {"name": "Baan Landai Fine Thai", "lat": 18.7915, "lon": 98.9892, "rating": 4.7, "type": "Restaurant", "color": GREEN, "maps": "https://maps.app.goo.gl/38"},
    {"name": "Khao Soi Maesai", "lat": 18.8001, "lon": 98.9814, "rating": 4.6, "type": "Restaurant", "color": GREEN, "maps": "https://maps.app.goo.gl/39"},
    {"name": "Khao Soi Lung Prakit", "lat": 18.7779, "lon": 98.9882, "rating": 4.6, "type": "Restaurant", "color": GREEN, "maps": "https://maps.app.goo.gl/40"},
    {"name": "SP Chicken", "lat": 18.7885, "lon": 98.9821, "rating": 4.5, "type": "Restaurant", "color": GREEN, "maps": "https://maps.app.goo.gl/41"},
    # Cafes
    {"name": "Akha Ama Phrasingh", "lat": 18.7884, "lon": 98.9832, "rating": 4.6, "type": "Cafe", "color": BROWN, "maps": "https://maps.app.goo.gl/34"},
    {"name": "The Baristro Asian Style", "lat": 18.7899, "lon": 98.9517, "rating": 4.7, "type": "Cafe", "color": BROWN, "maps": "https://maps.app.goo.gl/35"},
    {"name": "GRAPH ground", "lat": 18.7984, "lon": 98.9712, "rating": 4.7, "type": "Cafe", "color": BROWN, "maps": "https://maps.app.goo.gl/32"},
    {"name": "Into the Woods", "lat": 18.7948, "lon": 98.9867, "rating": 4.6, "type": "Cafe", "color": BROWN, "maps": "https://maps.app.goo.gl/29"}
]

df = pd.DataFrame(data)

# --- MAP SECTION (PyDeck) ---
# Define the layer for the dots
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[lon, lat]',
    get_color='color',
    get_radius=80,  # "Big" dots
    pickable=True,
)

# Set the initial view of the map
view_state = pdk.ViewState(
    latitude=18.788,
    longitude=98.985,
    zoom=13,
    pitch=0
)

# Render the map
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{name}\nType: {type}\nRating: {rating}"}
))

# --- DATA TABLES ---
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟢 Restaurants")
    res_df = df[df['type'] == 'Restaurant']
    st.dataframe(res_df[['name', 'rating', 'maps']], 
                 column_config={"maps": st.column_config.LinkColumn("Google Maps")},
                 hide_index=True, use_container_width=True)

with col2:
    st.subheader("🟤 Cafes")
    cafe_df = df[df['type'] == 'Cafe']
    st.dataframe(cafe_df[['name', 'rating', 'maps']], 
                 column_config={"maps": st.column_config.LinkColumn("Google Maps")},
                 hide_index=True, use_container_width=True)

st.sidebar.success("Settings: Custom Colors Applied")
