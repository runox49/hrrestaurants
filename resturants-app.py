import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Chiang Mai High-Rate Eats", page_icon="🍲", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTable { background-color: white; border-radius: 10px; }
    h1 { color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍲 Chiang Mai: 4.5★+ Restaurants")
st.markdown("A curated list of restaurants with over **500 reviews** and a rating of **4.5 or higher** on Google Maps.")

# Restaurant Data
data = [
    {"Name": "Baan Landai Fine Thai Cuisine", "Rating": 4.7, "Reviews": 1800, "Cuisine": "Fine Lanna/Thai", "Neighborhood": "Old City", "Highlight": "Signature Pork Ribs"},
    {"Name": "Khao Soi Maesai", "Rating": 4.6, "Reviews": 3200, "Cuisine": "Khao Soi / Noodles", "Neighborhood": "Santitham", "Highlight": "Authentic Curry Broth"},
    {"Name": "Khao Soi Lung Prakit", "Rating": 4.6, "Reviews": 4000, "Cuisine": "Khao Soi", "Neighborhood": "Wua Lai", "Highlight": "Beef Khao Soi (Netflix famous)"},
    {"Name": "Ginger Farm Kitchen", "Rating": 4.6, "Reviews": 2100, "Cuisine": "Organic Farm-to-Table", "Neighborhood": "Nimman", "Highlight": "Crispy Pork Belly"},
    {"Name": "SP Chicken", "Rating": 4.5, "Reviews": 2500, "Cuisine": "Isan Rotisserie", "Neighborhood": "Old City", "Highlight": "Garlic Roasted Chicken"},
    {"Name": "Huen Muan Jai", "Rating": 4.5, "Reviews": 4200, "Cuisine": "Traditional Lanna", "Neighborhood": "Santitham", "Highlight": "Lanna Appetizer Platter"},
    {"Name": "Khao Kha Moo Chang Phueak", "Rating": 4.5, "Reviews": 2100, "Cuisine": "Stewed Pork Leg", "Neighborhood": "North Gate", "Highlight": "The 'Cowboy Hat' Pork Leg"},
]

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filter Results")
selected_neighborhood = st.sidebar.multiselect("Select Neighborhood", options=df["Neighborhood"].unique(), default=df["Neighborhood"].unique())

# Filter data
filtered_df = df[df["Neighborhood"].isin(selected_neighborhood)]

# Display Interactive Table
st.subheader("Interactive Summary")
st.dataframe(filtered_df.sort_values(by="Rating", ascending=False), use_container_width=True, hide_index=True)

# Detailed View
st.divider()
st.subheader("🔍 Deep Dive")

cols = st.columns(2)
for i, row in filtered_df.iterrows():
    with cols[i % 2]:
        with st.expander(f"**{row['Name']}**"):
            st.write(f"**Rating:** ⭐ {row['Rating']} ({row['Reviews']:,}+ reviews)")
            st.write(f"**Cuisine:** {row['Cuisine']}")
            st.write(f"**Neighborhood:** {row['Neighborhood']}")
            st.info(f"💡 **Don't Miss:** {row['Highlight']}")

st.sidebar.info("Data curated for 2025. Ratings are subject to change on Google Maps live feed.")
