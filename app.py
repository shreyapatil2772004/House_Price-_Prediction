import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# -----------------------------
# Load Model
# -----------------------------

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")


model = load_model()


# -----------------------------
# Title
# -----------------------------

st.title("🏠 House Price Prediction")

st.write(
    "Enter the house details below to predict the house price."
)

st.divider()


# -----------------------------
# User Inputs
# -----------------------------

area = st.number_input(
    "Area (sq ft)",
    min_value=0,
    value=1600,
    step=50
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    value=3,
    step=1
)

age = st.number_input(
    "Age of House",
    min_value=0,
    value=3,
    step=1
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "age": [age]
    })

    prediction = model.predict(input_data)[0]

    st.success("Prediction Completed!")

    st.metric(
        "Predicted House Price",
        f"{prediction:,.2f}"
    )

    st.write("Input Data:")

    st.dataframe(input_data)