import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")

age=st.slider("Select your age:",0,100,25)

st.write(f"Your Age is {age}.")

options=['Python','Java','C++','JavaScript']
choice= st.selectbox("Choose your favourite language: ",options)
st.write(f"You selected {choice}.") 

if name:
    st.write(f"Hello, {name}")

data={
    "Name": ["Chetana","Arya","Aryan","Talat"],
    "Age": [28,23,26,29],
    "City": ["Mumbai","Pune","Delhi","Gurgaon"]

}

df= pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV File",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)