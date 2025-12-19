import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: 5+5 Elite List", page_icon="🍲", layout="wide")

# --- DATASET ---
data = [
    # RESTAURANTS (6 items for testing pagination)
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Fine Dining French Art-Plate", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Legendary Butterfly Pea Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Farm-to-table organic", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin Royal Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Superb Local Value", "Color": [46, 125, 50, 200]},
    {"Name": "Khao Soi Maesai", "Price": "฿", "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Lat": 18.8001, "Lon": 98.9814, "Note": "Gold Standard Khao Soi", "Color": [46, 125, 50, 200]},
    
    # CAFES (6 items for testing pagination)
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "World Latte Art Champ", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Artistic pour-over", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Perfect 5-star gem", "Color": [121, 85, 72, 200]},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Modern roastery", "Color": [121, 85, 72, 200]},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Legendary Local Beans", "Color": [121, 85, 72, 200]},
    {"Name": "Graph Ground", "Price": "฿฿", "Rating": 4.7, "Reviews": 1200, "Type": "Cafe", "Lat": 18.7984, "Lon": 98.9712, "Note": "Industrial Specialty Coffee", "Color": [121, 85, 72, 200]}
]

df = pd.DataFrame(data)

# --- SIDEBAR FILTERS ---
st.sidebar.header("Price Filter")
price_filter = st.sidebar.multiselect("Select Price", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])

# Filter original DF
filtered_df = df[df["Price"].isin(price_filter)]

# Split into two groups
res_df = filtered_df[filtered_df["Type"] == "Restaurant"]
caf_df = filtered_df[filtered_df["Type"] == "Cafe"]

# --- PAGINATION CALCULATIONS ---
items_per_page = 5
max_res_pages = (len(res_df) - 1) // items_per_page + 1
max_caf_pages = (len(caf_df) - 1) // items_per_page + 1
total_pages = max(max_res_pages, max_caf_pages)

if 'page' not in st.session_state:
    st.session_state.page = 1

# --- UI HEADER ---
st.title("🍲 Chiang Mai: The 5+5 Elite Guide")
st.markdown(f"Displaying up to **5 Restaurants** and **5 Cafes** per page.")

# Map
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13),
    layers=[pdk.Layer("ScatterplotLayer", filtered_df, get_position='[Lon, Lat]', get_color='Color', get_radius=120, pickable=True)],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}"}
))

# Navigation
st.divider()
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    if st.button("⬅️ Previous") and st.session_state.page > 1:
        st.session_state.page -= 1
with c2:
    st.write(f"### Page {st.session_state.page} of {total_pages}")
with c3:
    if st.button("Next ➡️") and st.session_state.page < total_pages:
        st.session_state.page += 1

# Slice Data
start = (st.session_state.page - 1) * items_per_page
end = start + items_per_page

current_res = res_df.iloc[start:end]
current_caf = caf_df.iloc[start:end]

# --- DEEP DIVE SECTION (Side-by-Side) ---
st.subheader("🔍 Deep Dive: Local Excellence")
col_res, col_caf = st.columns(2)

with col_res:
    st.markdown("### 🟢 Top Restaurants")
    for _, row in current_res.iterrows():
        with st.expander(f"{row['Name']} ({row['Price']})"):
            st.write(f"**Rating:** {row['Rating']}★ | **Reviews:** {row['Reviews']}")
            st.info(row['Note'])

with col_caf:
    st.markdown("### 🟤 Top Cafes")
    for _, row in current_caf.iterrows():
        with st.expander(f"{row['Name']} ({row['Price']})"):
            st.write(f"**Rating:** {row['Rating']}★ | **Reviews:** {row['Reviews']}")
            st.info(row['Note'])

# --- SUMMARY TABLE ---
st.subheader("📋 Page Summary")
combined_page = pd.concat([current_res, current_caf])
st.table(combined_page[["Name", "Type", "Price", "Rating"]])
