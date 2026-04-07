import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter house details:")

# Inputs (sliders for better UI)
area = st.slider("Square Footage", 500, 5000, 1500)
bedrooms = st.slider("Bedrooms", 1, 6, 3)
bathrooms = st.slider("Bathrooms", 1, 5, 2)

# Prediction
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    
    st.success(f"Estimated Price: ${prediction[0]:,.2f}")
