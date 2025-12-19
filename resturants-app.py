import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Chiang Mai: Elite Collection", page_icon="🍲", layout="wide")

# --- DATASET ---
data = [
    {"Name": "L'éléphant", "Price": "฿฿฿", "Rating": 4.7, "Reviews": 450, "Type": "Restaurant", "Lat": 18.7938, "Lon": 98.9725, "Note": "Fine Dining French Art-Plate", "Color": [46, 125, 50, 200]},
    {"Name": "Anchan Vegetarian", "Price": "฿฿", "Rating": 4.5, "Reviews": 850, "Type": "Restaurant", "Lat": 18.7966, "Lon": 98.9656, "Note": "Legendary Butterfly Pea Thai Food", "Color": [46, 125, 50, 200]},
    {"Name": "Garden to Table", "Price": "฿฿", "Rating": 4.9, "Reviews": 350, "Type": "Restaurant", "Lat": 18.7865, "Lon": 98.9904, "Note": "Farm-to-table organic experience", "Color": [46, 125, 50, 200]},
    {"Name": "Baan Landai Fine Thai", "Price": "฿฿", "Rating": 4.7, "Reviews": 1800, "Type": "Restaurant", "Lat": 18.7915, "Lon": 98.9892, "Note": "Michelin-recognized Royal Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Thai Food Good Taste", "Price": "฿", "Rating": 4.9, "Reviews": 650, "Type": "Restaurant", "Lat": 18.7883, "Lon": 98.9868, "Note": "Best value high-rating Thai", "Color": [46, 125, 50, 200]},
    {"Name": "Ristr8to Original", "Price": "฿฿", "Rating": 4.6, "Reviews": 4200, "Type": "Cafe", "Lat": 18.7991, "Lon": 98.9672, "Note": "World Latte Art Champion", "Color": [121, 85, 72, 200]},
    {"Name": "Gallery Drip Coffee", "Price": "฿฿", "Rating": 4.8, "Reviews": 1100, "Type": "Cafe", "Lat": 18.7902, "Lon": 98.9867, "Note": "Artistic pour-over specialty", "Color": [121, 85, 72, 200]},
    {"Name": "Sweet Home Coffee", "Price": "฿", "Rating": 5.0, "Reviews": 210, "Type": "Cafe", "Lat": 18.7830, "Lon": 98.9822, "Note": "Perfect 5-star cozy gem", "Color": [121, 85, 72, 200]},
    {"Name": "The Baristro Roaster", "Price": "฿฿", "Rating": 4.8, "Reviews": 950, "Type": "Cafe", "Lat": 18.8171, "Lon": 98.9993, "Note": "Industrial riverside roastery", "Color": [121, 85, 72, 200]},
    {"Name": "Akha Ama Phrasingh", "Price": "฿", "Rating": 4.6, "Reviews": 2800, "Type": "Cafe", "Lat": 18.7884, "Lon": 98.9832, "Note": "Famous sustainable local beans", "Color": [121, 85, 72, 200]},
    {"Name": "Khao Soi Maesai", "Price": "฿", "Rating": 4.6, "Reviews": 3200, "Type": "Restaurant", "Lat": 18.8001, "Lon": 98.9814, "Note": "The gold standard for Khao Soi", "Color": [46, 125, 50, 200]}
]

df = pd.DataFrame(data)

# --- FILTERS ---
st.sidebar.header("Global Filters")
price_filter = st.sidebar.multiselect("Price Range", ["฿", "฿฿", "฿฿฿"], default=["฿", "฿฿", "฿฿฿"])
type_filter = st.sidebar.multiselect("Type", ["Restaurant", "Cafe"], default=["Restaurant", "Cafe"])

filtered_df = df[(df["Price"].isin(price_filter)) & (df["Type"].isin(type_filter))]

# --- PAGINATION LOGIC ---
items_per_page = 5
total_pages = (len(filtered_df) // items_per_page) + (1 if len(filtered_df) % items_per_page > 0 else 0)

if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    if st.session_state.page < total_pages:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# --- UI ---
st.title("🍲 Chiang Mai: The Elite 4.5+ List")

# Map (Always shows all filtered results)
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(latitude=18.79, longitude=98.98, zoom=13),
    layers=[pdk.Layer("ScatterplotLayer", filtered_df, get_position='[Lon, Lat]', get_color='Color', get_radius=120, pickable=True)],
    tooltip={"text": "{Name}\n{Rating}★ | {Price}"}
))

# Pagination Controls
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("⬅️ Previous", on_click=prev_page, disabled=(st.session_state.page == 1))
with col2:
    st.write(f"**Page {st.session_state.page} of {total_pages}** (Showing {len(filtered_df)} total)")
with col3:
    st.button("Next ➡️", on_click=next_page, disabled=(st.session_state.page == total_pages))

# Slicing the dataframe for current page
start_idx = (st.session_state.page - 1) * items_per_page
end_idx = start_idx + items_per_page
page_df = filtered_df.iloc[start_idx:end_idx]

# --- THE DEEP DIVE SECTION ---
st.subheader("🔍 Deep Dive: Current Page Details")
for _, row in page_df.iterrows():
    with st.expander(f"{row['Name']} — {row['Rating']}★ ({row['Price']})"):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric("Reviews", f"{row['Reviews']:,}+")
            st.write(f"**Type:** {row['Type']}")
        with c2:
            st.write(f"**Why visit:** {row['Note']}")
            st.markdown(f"[📍 Open in Google Maps](https://www.google.com/maps/search/?api=1&query={row['Lat']},{row['Lon']})")

# Simplified Table for current page
st.subheader("📋 Quick List (Page View)")
st.table(page_df[["Name", "Type", "Price", "Rating"]])
