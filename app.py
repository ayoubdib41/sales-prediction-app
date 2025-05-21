import streamlit as st
import pandas as pd
import joblib

# Charger le pipeline
pipeline = joblib.load("sales_pipeline.pkl")

# Titre principal
st.title("📈 Prédiction des ventes - Superstore")

# 🎨 Style professionnel intégré
st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            color: #212529;
            font-family: 'Segoe UI', sans-serif;
        }

        h1, h2, h3 {
            color: #0d6efd;
        }

        input, select, textarea {
            border-radius: 8px !important;
            padding: 8px !important;
            font-size: 15px !important;
        }

        .stButton>button {
            background-color: #0d6efd;
            color: white;
            font-weight: bold;
            padding: 0.6rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #0b5ed7;
        }

        .stAlert {
            background-color: #e2f0d9;
            color: #155724;
            border-radius: 10px;
            padding: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Formulaire de saisie
st.subheader("🧾 Veuillez remplir les champs ci-dessous :")

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

# Préparer les données
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

# Lancer la prédiction
if st.button("🔮 Prédire les ventes"):
    prediction = pipeline.predict(input_data)
    st.success(f"📊 Vente prédite : {prediction[0]:.2f} $")
