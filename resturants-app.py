import streamlit as st
import pandas as pd
import pydeck as pdk

# Page configuration
st.set_page_config(page_title="Chiang Mai: Elite Selection", page_icon="🍲", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2e7d32; }
    .stSelectbox label { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍲 Chiang Mai: The High-Rate Collection")
st.markdown("Filter by price to find the perfect match. **Green** = Restaurants | **Brown** = Cafes.")

# --- DATASET WITH PRICE RANGES ---
GREEN = [46, 125, 50, 200]
BROWN = [121, 85, 72, 200]

data = [
    # RESTAURANTS
    {"Name": "Baan Landai Fine Thai", "Lat": 18.7915, "Lon": 98.9892, "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Color": GREEN, "Price": "฿฿", "Maps": "https://www.google.com/maps/contrib/110452326452262190497/reviews"},
    {"Name": "Khao Soi Maesai", "Lat": 18.8001, "Lon": 98.9814, "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Color": GREEN, "Price": "฿", "Maps": "https://maps.app.goo.gl/Zx8d3PER3hMfUndL78"},
    {"Name": "Thai Food Good Taste", "Lat": 18.7883, "Lon": 98.9868, "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Color": GREEN, "Price": "฿", "Maps": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sCi9DQUlRQUNvZENodHljRjlvT2toS2JrOXpiM3BRYUdoaU1FUnhNMGhXU1RCTk1FRRAB!2m1!1s0x30da3b0c1cde7b1d:0x40280d2f8656ec82"},
    {"Name": "Why Not? Italian", "Lat": 18.7968, "Lon": 98.9681, "Rating": 4.5, "Reviews": 1400, "Type": "Restaurant", "Color": GREEN, "Price": "฿฿", "Maps": "https://www.google.com/maps/contrib/108756061429900811603/reviews"},
    {"Name": "SP Chicken", "Lat": 18.7885, "Lon": 98.9821, "Rating": 4.5, "Reviews": 2500, "Type": "Restaurant", "Color": GREEN, "Price": "฿", "Maps": "https://maps.app.goo.gl/yKud3XbH6JvqeM3461"},
    {"Name": "Pari- Restaurant", "Lat": 18.7865, "Lon": 98.9821, "Rating": 4.7, "Reviews": 550, "Type": "Restaurant", "Color": GREEN, "Price": "฿฿฿", "Maps": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sCi9DQUlRQUNvZENodHljRjlvT2s4NWRYbHJRMGgzVVdWV1ZuUk5lbkphV0hCRU1tYxAB!2m1!1s0x30da3b0c1cde7b1d:0x40280d2f8656ec82"},
    {"Name": "Busarin", "Lat": 18.8006, "Lon": 98.9973, "Rating": 4.7, "Reviews": 400, "Type": "Restaurant", "Color": GREEN, "Price": "฿฿", "Maps": "https://www.google.com/maps/contrib/100183756779556124273/reviews"},
    
    # CAFES
    {"Name": "Akha Ama Phrasingh", "Lat": 18.7884, "Lon": 98.9832, "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Color": BROWN, "Price": "฿", "Maps": "https://maps.app.goo.gl/yKud3XbH6JvqeM3464"},
    {"Name": "Mitte Mitte", "Lat": 18.7923, "Lon": 98.9958, "Rating": 4.7, "Reviews": 850, "Type": "Cafe", "Color": BROWN, "Price": "฿฿", "Maps": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sCi9DQUlRQUNvZENodHljRjlvT25WNVRVWlZUa0ZTVnkxek16VnhTa1ZUU2tWc1ZIYxAB!2m1!1s0x30da3b0c1cde7b1d:0x40280d2f8656ec82"},
    {"Name": "Twenty Mar", "Lat": 18.7893, "Lon": 98.9879, "Rating": 4.9, "Reviews": 450, "Type": "Cafe", "Color": BROWN, "Price": "฿฿", "Maps": "https://www.google.com/maps/contrib/104370276563260845613/reviews"},
    {"Name": "Caramellow Cafe", "Lat": 18.7683, "Lon": 98.9810, "Rating": 4.9, "Reviews": 700, "Type": "Cafe", "Color": BROWN, "Price": "฿฿", "Maps": "https://maps.app.goo.gl/yKud3XbH6JvqeM3467"},
    {"Name": "Graph Ground", "Lat": 18.7984, "Lon": 98.9712, "Rating": 4.7, "Reviews": 1200, "Type": "Cafe", "Color": BROWN, "Price": "฿฿", "Maps": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sCi9DQUlRQUNvZENodHljRjlvT2s5bmEycEVjWEZRWm1wWFNtSkNSV3RPVkZoNmNXYxAB!2m1!1s0x30da3b0c1cde7b1d:0x40280d2f8656ec82"},
    {"Name": "Into the Woods", "Lat": 18.7948, "Lon": 98.9867, "Rating": 4.6, "Reviews": 950, "Type": "Cafe", "Color": BROWN, "Price": "฿฿", "Maps": "https://www.google.com/maps/contrib/102433406851714763362/reviews"}
]

df = pd.DataFrame(data)

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Results")
selected_types = st.sidebar.multiselect("Establishment Type", ["Restaurant", "Cafe"], default=["Restaurant", "Cafe"])
selected_prices = st.sidebar.multiselect("Price Range", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])

# Apply Filters
filtered_df = df[(df["Type"].isin(selected_types)) & (df["Price"].isin(selected_prices))]

# --- 1. THE MAP ---
st.subheader(f"🗺️ Viewing {len(filtered_df)} Locations")
view_state = pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13)
layer = pdk.Layer(
    "ScatterplotLayer",
    filtered_df,
    get_position='[Lon, Lat]',
    get_color='Color',
    get_radius=90,
    pickable=True,
)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{Name}\nPrice: {Price}\nRating: {Rating}★"}))

# --- 2. THE TABLE ---
st.subheader("📊 Interactive Table")
st.dataframe(
    filtered_df[["Name", "Type", "Price", "Rating", "Reviews", "Maps"]],
    column_config={"Maps": st.column_config.LinkColumn("Google Maps")},
    hide_index=True, use_container_width=True
)

# --- 3. THE DETAILS ---
st.divider()
if not filtered_df.empty:
    cols = st.columns(3)
    for i, row in filtered_df.reset_index().iterrows():
        with cols[i % 3]:
            with st.expander(f"**{row['Name']}** ({row['Price']})"):
                st.write(f"**Rating:** {row['Rating']}★")
                st.write(f"**Reviews:** {row['Reviews']:,}+")
                st.markdown(f"[📍 Google Maps Link]({row['Maps']})")
else:
    st.warning("No matches found for the selected filters.")
