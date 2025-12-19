import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: The 4.5+ Collection", page_icon="📍", layout="wide")

# --- DATASET (4.5★ / 200+ Reviews) ---
data = [
    # RESTAURANTS
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Fine Dining French Art-Plate", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Best Butterfly Pea Pad Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Farm-fresh organic dishes", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin-recognized Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Superb Local Taste", "Color": [46, 125, 50, 200]},
    
    # CAFES
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "World Latte Art Champ", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Inside the Culture Center", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Cozy, perfectionist coffee", "Color": [121, 85, 72, 200]},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Modern Industrial Roastery", "Color": [121, 85, 72, 200]},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Legendary Hill-Tribe Coffee", "Color": [121, 85, 72, 200]},
]

df = pd.DataFrame(data)

# --- SIDEBAR ---
st.sidebar.header("Filter Results")
price_filter = st.sidebar.multiselect("Price Range", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])
type_filter = st.sidebar.multiselect("Type", ["Restaurant", "Cafe"], default=["Restaurant", "Cafe"])

# Apply Filters
filtered_df = df[(df["Price"].isin(price_filter)) & (df["Type"].isin(type_filter))]

# --- UI ---
st.title("📍 Chiang Mai: Top-Rated Favorites")
st.markdown(f"Viewing **{len(filtered_df)}** elite spots (4.5+ ★ | 200+ Reviews).")

# Map with explicit Color column usage to avoid JS unclosed bracket errors
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13, pitch=0),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            filtered_df,
            get_position='[Lon, Lat]',
            get_color='Color',  # Fixed: Reference the pre-calculated column
            get_radius=120,
            pickable=True,
        ),
    ],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}\n{Note}"}
))

# Table
st.subheader("📋 Discovery List")
st.dataframe(filtered_df[["Name", "Type", "Price", "Rating", "Reviews", "Note"]], use_container_width=True, hide_index=True)
