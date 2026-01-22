# 🛍️ Recofy: Smart Retail Recommendation & Customer Segmentation App

Recofy is a smart, ML-powered retail assistant built as part of the **Shopper Spectrum** project. It combines product recommendation and customer segmentation into a single, cleanly designed web application.

The goal was simple: **help retailers and analysts make better decisions** by providing instant, intelligent insights — whether it’s finding the next product to recommend or understanding the type of customer they’re dealing with.

---

## 🔗 Live Deployment

🚀 **App is Live on Streamlit:**  
👉 [https://recofy-xrz3xhzekhru49x3dcmy9s.streamlit.app](https://recofy-xrz3xhzekhru49x3dcmy9s.streamlit.app)

Deployed via [Streamlit Cloud](https://streamlit.io/cloud) using GitHub integration.

---

## 🧠 What Recofy Does

Recofy offers **two intelligent modules**:

### 1. 📦 Product Recommendation  
- Enter a product keyword  
- The app matches it using `product_code_map.pkl`  
- It then finds top 5 similar items from a **cosine similarity matrix**  
- Recommends visually with product names and codes

### 2. 👤 Customer Segmentation  
- Input RFM values (Recency, Frequency, Monetary)  
- Uses a trained **KMeans clustering model** and `MinMaxScaler`  
- Predicts customer cluster & human-friendly label like:
  - `High-Value Shopper`
  - `At-Risk Shopper`
  - `Occasional Shopper`
  - `Regular Shopper`

---

## 💻 Implementation Overview

- **Built Using**: `Streamlit` + `Python`  
- **Styled With**: Bootstrap icons, Google Fonts, responsive CSS  
- **ML Models Used**:
  - KMeans for RFM-based segmentation (`best_kmeans_model.pkl`)
  - Cosine similarity matrix for item-item recommendation (`item_similarity_matrix.pkl`)

### Custom Styling Includes:
- Light/Dark Mode toggle  
- Sidebar navigation  
- Clean white text and medical-themed color palette  
- Responsive layout for all screen sizes

---

## 📁 Folder Structure

Recofy/
│
├── app/
│ ├── streamlit_app.py # Main web app
│ ├── assets/
│ │ ├── styles.css # All custom UI styling
│ │ ├── recofy_logo.png # Branded app logo
│
├── models/
│ ├── item_similarity_matrix.pkl
│ ├── product_code_map.pkl
│ ├── best_kmeans_model.pkl
│ ├── rfm_scaler.pkl
│
├── .streamlit/
│ └── config.toml # App layout settings
├── README.md
├── requirements.txt


---
Working Website screenshot :

<img width="1919" height="1007" alt="Screenshot 2025-08-03 191938" src="https://github.com/user-attachments/assets/68759d48-080d-4388-b3d8-5607f74c294f" />
<img width="1919" height="1005" alt="Screenshot 2025-08-03 192005" src="https://github.com/user-attachments/assets/6aecd5c0-ee69-4f5d-b357-4789779665c0" />
<img width="1919" height="1011" alt="Screenshot 2025-08-03 192049" src="https://github.com/user-attachments/assets/06034921-aee8-4c08-ade5-26d4b77348d5" />



---
## 📦 How to Run Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/tanushreedhananjayb/Recofy.git
cd Recofy

# Step 2: Install required packages
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app/streamlit_app.py

🛠 Tech Stack :
Frontend: Streamlit, HTML/CSS, Bootstrap Icons

Backend: Python (pandas, NumPy, scikit-learn, joblib)

ML Models: KMeans (for customer clustering), Cosine similarity (for product recommendation)

Deployment: Streamlit Cloud

Version Control: Git + GitHub

💡 Behind the Project
Recofy was developed as a part of a broader project to explore intelligent automation in retail analytics — using real-world data to make business insights more accessible and interactive.

Whether it's helping a business identify its most loyal customers or recommending the next best product to push, this app combines machine learning with simplicity.

👤 Author
Tanushree Dhananjay Bhamare
Final Year B.Tech (CSBS)
Data Science • Machine Learning • Full-Stack Enthusiast
🔗 LinkedIn - https://www.linkedin.com/in/tanushree-dhananjay-bhamare-9219b724b/


“Recofy helps retail decisions happen faster, smarter — and more intuitively. Built to be simple. Designed to be powerful.”
