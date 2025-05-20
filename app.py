
import streamlit as st
import pandas as pd
import joblib

# Chargement des modèles
model = joblib.load("xgboost_model.pkl")
scaler = joblib.load("scaler.pkl")
columns_reference = joblib.load("columns_reference.pkl")

# Titre de l’application
st.title("📈 Prédiction des ventes - Superstore")

# Saisie utilisateur
st.subheader("🧾 Veuillez remplir les champs ci-dessous :")

year = st.number_input("Année de commande", min_value=2015, max_value=2025, value=2018)
month = st.selectbox("Mois", list(range(1, 13)))
quantity = st.slider("Quantité", 1, 100, 1)
discount = st.slider("Remise (%)", 0.0, 0.9, 0.1)
profit = st.number_input("Profit", value=100.0)

category = st.selectbox("Catégorie", ['Furniture', 'Office Supplies', 'Technology'])
sub_category = st.selectbox("Sous-catégorie", ['Bookcases', 'Chairs', 'Phones', 'Binders', 'Tables', 'Storage', 'Accessories', 'Paper'])
region = st.selectbox("Région", ['East', 'West', 'Central', 'South'])
segment = st.selectbox("Segment", ['Consumer', 'Corporate', 'Home Office'])
ship_mode = st.selectbox("Mode de livraison", ['Standard Class', 'Second Class', 'First Class', 'Same Day'])

# Fonction de préparation
def prepare_input(df_input, columns_reference, scaler):
    df_encoded = pd.get_dummies(df_input)
    for col in columns_reference:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[columns_reference]
    df_scaled = scaler.transform(df_encoded)
    return df_scaled

# Prédiction
if st.button("🔮 Prédire les ventes"):
    user_input = pd.DataFrame([{
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
    
    X_ready = prepare_input(user_input, columns_reference, scaler)
    prediction = model.predict(X_ready)
    st.success(f"💰 Vente estimée : {prediction[0]:.2f} $")
