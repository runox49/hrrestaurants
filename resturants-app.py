import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: Custom Elite Guide", page_icon="🍲", layout="wide")

# --- EXPANDED DATASET ---
data = [
    # RESTAURANTS
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.7725, "Note": "Fine Dining French", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Legendary Vegan Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Farm-fresh organic", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin Royal Thai", "Color": [46, 125, 50, 200]},
    {"Name": "PARI-", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 550, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9821, "Note": "Modern Asian Fine Dining", "Color": [46, 125, 50, 200]},
    
    # CAFES
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "Latte Art Champion", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Specialty Manual Drip", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Top-rated micro-roastery", "Color": [121, 85, 72, 200]},
    {"Name": "Twenty Mar", "Price": "฿฿", "Rating": 4.9, "Reviews": 450, "Type": "Cafe", "Lat": 18.7893, "Lon": 98.9879, "Note": "Minimalist art space", "Color": [121, 85, 72, 200]},
    {"Name": "Caramellow Cafe", "Price": "฿฿", "Rating": 4.9, "Reviews": 700, "Type": "Cafe", "Lat": 18.7683, "Lon": 98.9810, "Note": "Peaceful garden brunch", "Color": [121, 85, 72, 200]},
]

df = pd.DataFrame(data)

# --- SIDEBAR: THREE BUTTONS ---
st.sidebar.title("Choose Your Vibe")
vibe = st.sidebar.radio("Show Me:", ["Both", "Restaurants", "Cafes"], horizontal=False)

# Filtering logic
if vibe == "Restaurants":
    filtered_df = df[df["Type"] == "Restaurant"]
elif vibe == "Cafes":
    filtered_df = df[df["Type"] == "Cafe"]
else:
    filtered_df = df

# --- MAP SECTION ---
st.title(f"📍 Explore Chiang Mai: {vibe}")
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13),
    layers=[pdk.Layer("ScatterplotLayer", filtered_df, get_position='[Lon, Lat]', get_color='Color', get_radius=110, pickable=True)],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}"}
))

# --- LISTINGS & DEEP DIVE ---
st.divider()

if vibe == "Both":
    col_res, col_caf = st.columns(2)
    with col_res:
        st.subheader("🟢 Restaurants")
        res_list = filtered_df[filtered_df["Type"] == "Restaurant"]
        st.table(res_list[["Name", "Rating", "Price"]])
        st.markdown("---")
        for _, row in res_list.iterrows():
            with st.expander(f"Deep Dive: {row['Name']}"):
                st.write(row['Note'])
                st.markdown(f"[📍 Google Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")
                
    with col_caf:
        st.subheader("🟤 Cafes")
        caf_list = filtered_df[filtered_df["Type"] == "Cafe"]
        st.table(caf_list[["Name", "Rating", "Price"]])
        st.markdown("---")
        for _, row in caf_list.iterrows():
            with st.expander(f"Deep Dive: {row['Name']}"):
                st.write(row['Note'])
                st.markdown(f"[📍 Google Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")

else:
    # SINGLE VIEW (Only Restaurants OR Only Cafes)
    icon = "🟢" if vibe == "Restaurants" else "🟤"
    st.subheader(f"{icon} {vibe} List")
    st.table(filtered_df[["Name", "Rating", "Price", "Reviews"]])
    
    st.divider()
    st.subheader(f"🔍 {vibe} Deep Dive")
    for _, row in filtered_df.iterrows():
        with st.expander(f"{row['Name']} — {row['Rating']}★ Details"):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("Reviews", f"{row['Reviews']:,}")
            with col2:
                st.info(row['Note'])
                st.markdown(f"[📍 View Location on Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")
