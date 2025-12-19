import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: The Elite 10", page_icon="📍", layout="wide")

# --- EXPANDED DATASET (4.5★ / 200+ Reviews) ---
# Colors: [46, 125, 50] (Green) for Restaurants, [121, 85, 72] (Brown) for Cafes
data = [
    # --- RESTAURANTS ---
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Fine Dining French Art-Plate", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Butterfly Pea Pad Thai Specialist", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Organic farm-fresh fusion", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin-recognized Royal Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Excellent local Northern taste", "Color": [46, 125, 50, 200]},
    {"Name": "Khao Soi Maesai", "Price": "฿", "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Lat": 18.8001, "Lon": 98.9814, "Note": "The gold standard for Khao Soi", "Color": [46, 125, 50, 200]},
    {"Name": "SP Chicken", "Price": "฿", "Rating": 4.5, "Reviews": 1400, "Type": "Restaurant", "Lat": 18.7885, "Lon": 98.9819, "Note": "Famous Garlic Roasted Chicken", "Color": [46, 125, 50, 200]},
    {"Name": "Huen Phen", "Price": "฿฿", "Rating": 4.5, "Reviews": 2100, "Type": "Restaurant", "Lat": 18.7861, "Lon": 98.9858, "Note": "Classic Old City Northern Food", "Color": [46, 125, 50, 200]},
    {"Name": "Ginger & Kafe", "Price": "฿฿฿", "Rating": 4.5, "Reviews": 1200, "Type": "Restaurant", "Lat": 18.7928, "Lon": 98.9932, "Note": "Boutique dining & cocktails", "Color": [46, 125, 50, 200]},
    {"Name": "Tong Tem Toh", "Price": "฿฿", "Rating": 4.5, "Reviews": 4800, "Type": "Restaurant", "Lat": 18.7995, "Lon": 98.9682, "Note": "Nimman's most popular Thai BBQ", "Color": [46, 125, 50, 200]},

    # --- CAFES ---
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "World Latte Art Champ", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Artistic manual drip focus", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Exceptional micro-roastery", "Color": [121, 85, 72, 200]},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Minimalist riverside industrial", "Color": [121, 85, 72, 200]},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Socially conscious tribal beans", "Color": [121, 85, 72, 200]},
    {"Name": "Graph Ground", "Price": "฿฿", "Rating": 4.7, "Reviews": 1200, "Type": "Cafe", "Lat": 18.7984, "Lon": 98.9712, "Note": "Creative coffee concoctions", "Color": [121, 85, 72, 200]},
    {"Name": "Fern Forest Cafe", "Price": "฿฿", "Rating": 4.4, "Reviews": 2300, "Type": "Cafe", "Lat": 18.7934, "Lon": 98.9820, "Note": "Lush garden with great cakes", "Color": [121, 85, 72, 200]},
    {"Name": "Ministry of Roasters", "Price": "฿฿", "Rating": 4.9, "Reviews": 380, "Type": "Cafe", "Lat": 18.7897, "Lon": 98.9961, "Note": "Serious beans for enthusiasts", "Color": [121, 85, 72, 200]},
    {"Name": "Twenty Mar", "Price": "฿฿", "Rating": 4.9, "Reviews": 320, "Type": "Cafe", "Lat": 18.7893, "Lon": 98.9879, "Note": "Aesthetic minimalist haven", "Color": [121, 85, 72, 200]},
    {"Name": "Versailles de Flore", "Price": "฿฿", "Rating": 4.5, "Reviews": 450, "Type": "Cafe", "Lat": 18.7954, "Lon": 98.9791, "Note": "Neo-Renaissance architecture", "Color": [121, 85, 72, 200]},
]

df = pd.DataFrame(data)

# --- FILTERS ---
st.sidebar.header("Navigation & Filters")
price_filter = st.sidebar.multiselect("Price Range", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])

# Grouping logic
filtered_df = df[df["Price"].isin(price_filter)]
res_df = filtered_df[filtered_df["Type"] == "Restaurant"]
caf_df = filtered_df[filtered_df["Type"] == "Cafe"]

# --- PAGINATION ---
items_per_page = 5
total_pages = max(((len(res_df)-1)//items_per_page + 1) if not res_df.empty else 1, 
                  ((len(caf_df)-1)//items_per_page + 1) if not caf_df.empty else 1)

if 'page' not in st.session_state:
    st.session_state.page = 1

# Reset page if it exceeds total_pages after filtering
if st.session_state.page > total_pages:
    st.session_state.page = 1

# --- UI DISPLAY ---
st.title("📍 Chiang Mai: The Elite 4.5★ Collection")
st.info(f"Showing {len(res_df)} Restaurants and {len(caf_df)} Cafes.")

# Map Section
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13, pitch=40),
    layers=[pdk.Layer("ScatterplotLayer", filtered_df, get_position='[Lon, Lat]', get_color='Color', get_radius=110, pickable=True)],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}\n{Note}"}
))

# Pagination Buttons
st.divider()
nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
with nav_col1:
    if st.button("⬅️ Prev Page") and st.session_state.page > 1:
        st.session_state.page -= 1
with nav_col2:
    st.markdown(f"<center><h3>Page {st.session_state.page} / {total_pages}</h3></center>", unsafe_allow_html=True)
with nav_col3:
    if st.button("Next Page ➡️") and st.session_state.page < total_pages:
        st.session_state.page += 1

# Slice data for the current page
start = (st.session_state.page - 1) * items_per_page
current_res = res_df.iloc[start:start+items_per_page]
current_caf = caf_df.iloc[start:start+items_per_page]

# --- DUAL DEEP DIVE ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🟢 Top Restaurants")
    for _, row in current_res.iterrows():
        with st.expander(f"🍴 {row['Name']} ({row['Rating']}★)"):
            st.write(f"**Price:** {row['Price']} | **Reviews:** {row['Reviews']:,}")
            st.caption(row['Note'])
            st.markdown(f"[🗺️ View on Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")

with col_right:
    st.subheader("🟤 Top Cafes")
    for _, row in current_caf.iterrows():
        with st.expander(f"☕ {row['Name']} ({row['Rating']}★)"):
            st.write(f"**Price:** {row['Price']} | **Reviews:** {row['Reviews']:,}")
            st.caption(row['Note'])
            st.markdown(f"[🗺️ View on Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")
