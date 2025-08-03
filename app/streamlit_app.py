# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import time
import os

# PAGE CONFIG
st.set_page_config(
    page_title="Recofy",
    page_icon="app/assets/recofy_logo.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD STYLES ---
css_path = os.path.join("app", "assets", "styles.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("app/assets/recofy_logo.png", width=120)
st.sidebar.markdown("## Recofy")
st.sidebar.caption("Predict. Recommend. Thrive.")

# ✅ FIXED: Define navigation
navigation = st.sidebar.radio("Navigation", ["Home", "Product Recommendation", "Customer Segmentation"])

# ✅ Toggle for light/dark mode
light_mode = st.sidebar.toggle("Light Mode 🌞", value=False)

if light_mode:
    st.markdown("""
        <style>
        body, .main, .block-container {
            background-color: #f4f4f4 !important;
            color: #000 !important;
        }
        .recommend-box {
            background-color: #ffffff !important;
            color: #000 !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            color: #000 !important;
        }
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stRadio > div,
        section[data-testid="stSidebar"] .stRadio div span {
            color: #000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- MAIN HEADER ---
st.markdown("<div class='header-title'>Welcome to Recofy – Your Smart Retail Companion!</div>", unsafe_allow_html=True)

# --- LOAD MODELS ---
try:
    item_sim_df = joblib.load("models/item_similarity_matrix.pkl")
    product_map = joblib.load("models/product_code_map.pkl")
    kmeans_model = joblib.load("models/best_kmeans_model.pkl")
    scaler = joblib.load("models/rfm_scaler.pkl")
except Exception as e:
    st.error(f"⚠️ Error loading models: {e}")

# --- HOME PAGE ---
if navigation == "Home":
    st.markdown("""
        <div class='home-card'>
            <h3>Explore Recofy</h3>
            <ul>
                <li><i class="bi bi-box-seam"></i> Product Recommendation</li>
                <li><i class="bi bi-person-lines-fill"></i> Customer Segmentation</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# --- PRODUCT RECOMMENDATION ---
elif navigation == "Product Recommendation":
    st.subheader("Product Recommendation")
    product_input = st.text_input("Enter a product keyword")

    def get_matches(query):
        return {code: name for code, name in product_map.items() if query.lower() in name.lower()}

    if st.button("Find Recommendations"):
        if product_input:
            matches = get_matches(product_input)
            if matches:
                selected_code = list(matches.keys())[0]
                st.success(f"Matched: `{selected_code}` — {matches[selected_code]}")

                similar_items = item_sim_df[selected_code].sort_values(ascending=False)[1:6]
                st.markdown("#### Top 5 Similar Products:")
                for i, (code, _) in enumerate(similar_items.items(), 1):
                    name = product_map.get(code, "Unknown")
                    st.markdown(f"""
                        <div class='recommend-box'>
                            <i class="bi bi-caret-right-square-fill"></i> {i}. <strong>{name}</strong> 
                            <br><small>Code: {code}</small>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("No similar products found.")
        else:
            st.info("Enter a keyword to get started.")

# --- CUSTOMER SEGMENTATION ---
elif navigation == "Customer Segmentation":
    st.subheader("Customer Segmentation")

    r = st.number_input("Recency (days since last purchase)", min_value=0)
    f = st.number_input("Frequency (number of purchases)", min_value=0)
    m = st.number_input("Monetary (total spend)", min_value=0.0)

    def label_cluster(r, f, m):
        if r < 40 and f > 10 and m > 1000:
            return "High-Value Shopper"
        elif r < 80 and f > 4:
            return "Regular Shopper"
        elif r > 180 and f < 2:
            return "At-Risk Shopper"
        else:
            return "Occasional Shopper"

    if st.button("Predict Segment"):
        with st.spinner("Predicting segment..."):
            time.sleep(1.2)
            input_scaled = scaler.transform([[r, f, m]])
            cluster = kmeans_model.predict(input_scaled)[0]
            segment = label_cluster(r, f, m)

            st.success(f"Segment ID: **{cluster}**")
            st.markdown(f"**This customer belongs to:** `{segment}`")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div class='footer'>Built by Tanushree</div>", unsafe_allow_html=True)
