import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: Elite 5+5", page_icon="📍", layout="wide")

# --- DATASET (4.5★+ / 200+ Reviews) ---
data = [
    # RESTAURANTS
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Art-focused French Fine Dining", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Famous Butterfly Pea Pad Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Fresh organic farm-to-plate", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin-rated Royal Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Authentic and great value", "Color": [46, 125, 50, 200]},
    {"Name": "Khao Soi Maesai", "Price": "฿", "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Lat": 18.8001, "Lon": 98.9814, "Note": "Local favorite for curry noodles", "Color": [46, 125, 50, 200]},
    {"Name": "SP Chicken", "Price": "฿", "Rating": 4.5, "Reviews": 2500, "Type": "Restaurant", "Lat": 18.7885, "Lon": 98.9821, "Note": "Garlic rotisserie chicken", "Color": [46, 125, 50, 200]},
    {"Name": "Reform Kafé", "Price": "฿฿", "Rating": 4.7, "Reviews": 1400, "Type": "Restaurant", "Lat": 18.7945, "Lon": 98.9843, "Note": "Garden-based vegan haven", "Color": [46, 125, 50, 200]},
    {"Name": "Another World", "Price": "฿฿", "Rating": 4.9, "Reviews": 280, "Type": "Restaurant", "Lat": 18.7842, "Lon": 98.9919, "Note": "Hidden garden oasis dining", "Color": [46, 125, 50, 200]},
    {"Name": "PARI-", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 550, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9821, "Note": "Upscale fine dining experience", "Color": [46, 125, 50, 200]},

    # CAFES
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "Award-winning latte art", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Inside Cultural Center", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Hidden micro-roastery gem", "Color": [121, 85, 72, 200]},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Modern riverside vibes", "Color": [121, 85, 72, 200]},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Socially conscious tribal coffee", "Color": [121, 85, 72, 200]},
    {"Name": "Twenty Mar", "Price": "฿฿", "Rating": 4.9, "Reviews": 450, "Type": "Cafe", "Lat": 18.7893, "Lon": 98.9879, "Note": "Aesthetic minimalist specialty", "Color": [121, 85, 72, 200]},
    {"Name": "Caramellow Cafe", "Price": "฿฿", "Rating": 4.9, "Reviews": 700, "Type": "Cafe", "Lat": 18.7683, "Lon": 98.9810, "Note": "Peaceful garden and brunch", "Color": [121, 85, 72, 200]},
    {"Name": "Kilim Coffee House", "Price": "฿฿", "Rating": 4.9, "Reviews": 400, "Type": "Cafe", "Lat": 18.7901, "Lon": 98.9999, "Note": "Middle Eastern style decor", "Color": [121, 85, 72, 200]},
    {"Name": "Graph Ground", "Price": "฿฿", "Rating": 4.7, "Reviews": 1200, "Type": "Cafe", "Lat": 18.7984, "Lon": 98.9712, "Note": "Nitro brew & industrial design", "Color": [121, 85, 72, 200]},
    {"Name": "Mitte Mitte", "Price": "฿฿", "Rating": 4.7, "Reviews": 850, "Type": "Cafe", "Lat": 18.7923, "Lon": 98.9958, "Note": "Famous for artisanal bagels", "Color": [121, 85, 72, 200]},
]

df = pd.DataFrame(data)

# --- SIDEBAR TOGGLE LOGIC ---
st.sidebar.title("View Mode")
view_mode = st.sidebar.radio("Show Me:", ["Both", "Restaurants Only", "Cafes Only"])

if view_mode == "Restaurants Only":
    filtered_df = df[df["Type"] == "Restaurant"]
elif view_mode == "Cafes Only":
    filtered_df = df[df["Type"] == "Cafe"]
else:
    filtered_df = df

# --- PAGINATION ---
items_per_group = 5
res_all = filtered_df[filtered_df["Type"] == "Restaurant"]
caf_all = filtered_df[filtered_df["Type"] == "Cafe"]

# Total pages needed
max_p = max(((len(res_all)-1)//items_per_group + 1) if not res_all.empty else 1, 
            ((len(caf_all)-1)//items_per_group + 1) if not caf_all.empty else 1)

if 'page' not in st.session_state: st.session_state.page = 1
if st.session_state.page > max_p: st.session_state.page = 1

# --- UI ---
st.title("🗺️ Chiang Mai Elite: 5+5 Discovery")

# Map
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13, pitch=45),
    layers=[pdk.Layer("ScatterplotLayer", filtered_df, get_position='[Lon, Lat]', get_color='Color', get_radius=110, pickable=True)],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}"}
))

# Nav Buttons
st.divider()
c1, c2, c3 = st.columns([1, 2, 1])
with c1: 
    if st.button("⬅️ Previous") and st.session_state.page > 1: st.session_state.page -= 1
with c2: 
    st.markdown(f"<center><b>Page {st.session_state.page} / {max_p}</b></center>", unsafe_allow_html=True)
with c3: 
    if st.button("Next ➡️") and st.session_state.page < max_p: st.session_state.page += 1

# Display Logic
start = (st.session_state.page - 1) * items_per_group
current_res = res_all.iloc[start : start + items_per_group]
current_caf = caf_all.iloc[start : start + items_per_group]

# --- DEEP DIVE ---
col_res, col_caf = st.columns(2)
with col_res:
    st.subheader("🟢 Restaurants")
    for _, r in current_res.iterrows():
        with st.expander(f"🍴 {r['Name']} ({r['Rating']}★)"):
            st.write(f"**Price:** {r['Price']} | {r['Note']}")
            st.markdown(f"[📍 Google Maps](https://www.google.com/maps/search/?api=1&query={r['Lat']},{r['Lon']})")

with col_caf:
    st.subheader("🟤 Cafes")
    for _, r in current_caf.iterrows():
        with st.expander(f"☕ {r['Name']} ({r['Rating']}★)"):
            st.write(f"**Price:** {r['Price']} | {r['Note']}")
            st.markdown(f"[📍 Google Maps](https://www.google.com/maps/search/?api=1&query={r['Lat']},{r['Lon']})")
