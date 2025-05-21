import streamlit as st
import pandas as pd
import joblib

# Chargement du pipeline entraîné
pipeline = joblib.load("sales_pipeline.pkl")

# Titre de l'app
st.title("📈 Prédiction des ventes - Superstore")
# 🎨 Style professionnel du fond et de la police
st.markdown("""
    <style>
    /* Fond général */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        color: #212529;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Titres */
    h1, h2, h3 {
        color: #0d6efd;
    }

    /* Widgets (inputs, sliders, etc.) */
    .stTextInput > div > div > input,
    .stNumberInput input,
    .stSelectbox div,
    .stButton button {
        border-radius: 8px;
        padding: 0.4rem;
        font-size: 0.95rem;
    }

    /* Boutons */
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #0b5ed7;
    }

    /* Encadré de la prédiction */
    .stAlert {
        background-color: #e2f0d9;
        color: #155724;
        border-radius: 10px;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown(""" ... """, unsafe_allow_html=True)

st.subheader("🧾 Veuillez remplir les champs ci-dessous :")

# Interface utilisateur
year = st.number_input("Année de commande", min_value=2015, max_value=2025, value=2018)
month = st.selectbox("Mois", list(range(1, 13)), index=0)
quantity = st.slider("Quantité", min_value=1, max_value=100, value=1)
discount = st.slider("Remise (%)", min_value=0.0, max_value=0.9, step=0.05, value=0.0)
profit = st.number_input("Profit", value=100.0)

category = st.selectbox("Catégorie", ["Furniture", "Office Supplies", "Technology"])
sub_category = st.selectbox("Sous-catégorie", ["Bookcases", "Chairs", "Phones", "Binders", "Storage", "Accessories"])
region = st.selectbox("Région", ["East", "West", "Central", "South"])
segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])
ship_mode = st.selectbox("Mode de livraison", ["Standard Class", "Second Class", "First Class", "Same Day"])

# Données d'entrée
input_data = pd.DataFrame([{
    "Order_Year": year,
    "Order_Month": month,
    "Quantity": quantity,
    "Discount": discount,
    "Profit": profit,
    "Category": category,
    "Sub-Category": sub_category,
    "Region": region,
    "Segment": segment,
    "Ship Mode": ship_mode
}])

# Prédiction
if st.button("🔮 Prédire les ventes"):
    prediction = pipeline.predict(input_data)
    st.success(f"📊 Vente prédite : {prediction[0]:.2f} $")
