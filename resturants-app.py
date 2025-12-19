import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: The 4.5+ Collection", page_icon="📍", layout="wide")

# --- EXPANDED DATASET (4.5★ / 200+ Reviews) ---
data = [
    # RESTAURANTS
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Fine Dining French Art-Plate"},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Best Butterfly Pea Pad Thai"},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Farm-fresh organic dishes"},
    {"Name": "Another World", "Price": "฿฿", "Rating": 4.9, "Reviews": 280, "Type": "Restaurant", "Lat": 18.7842, "Lon": 98.9919, "Note": "Hidden Garden Oasis"},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin-recognized Thai"},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Superb Local Taste"},
    
    # CAFES
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "World Latte Art Champ"},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Inside the Culture Center"},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Cozy, perfectionist coffee"},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Modern Industrial Roastery"},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Legendary Hill-Tribe Coffee"},
]

df = pd.DataFrame(data)

# --- SIDEBAR ---
st.sidebar.title("Filters")
price_filter = st.sidebar.multiselect("Price Range", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])
type_filter = st.sidebar.multiselect("Type", ["Restaurant", "Cafe"], default=["Restaurant", "Cafe"])

# Logic
filtered_df = df[(df["Price"].isin(price_filter)) & (df["Type"].isin(type_filter))]

# --- UI ---
st.title("📍 Chiang Mai: Top-Rated Favorites")
st.markdown(f"Now showing **{len(filtered_df)}** spots with 4.5+ stars and 200+ reviews.")

# Map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13, pitch=45),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            filtered_df,
            get_position='[Lon, Lat]',
            get_color='[46, 125, 50, 200] if Type=="Restaurant" else [121, 85, 72, 200]',
            get_radius=100,
            pickable=True,
        ),
    ],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}\n{Note}"}
))

# Table
st.dataframe(filtered_df[["Name", "Price", "Rating", "Reviews", "Note"]], use_container_width=True, hide_index=True)
