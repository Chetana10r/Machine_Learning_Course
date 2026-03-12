import streamlit as st
import requests

st.title("Linear Regression Fare Prediction (Streamlit + Flask)")

age = st.number_input("Age")
sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
embarked = st.selectbox("Embarked (0,1,2)", [0, 1, 2])
class1 = st.selectbox("Class1", [0, 1])
class2 = st.selectbox("Class2", [0, 1])
class3 = st.selectbox("Class3", [0, 1])

if st.button("Predict Fare"):
    features = [age, sex, embarked, class1, class2, class3]
    
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={"features": features}
    )
    
    result = response.json()
    st.success(f"Predicted Fare: {result['predicted_fare']}")
