import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Welcome to streamlit tutorials!")

st.header("1) first example to print the dataframe and a line chart using that dataframe")

df = pd.DataFrame(
    np.random.randn(20, 3), columns=['first', 'second', 'third']
)

st.write("Here is the dataframe")
st.write(df)

st.write("and here is the line chart from above data")
st.line_chart(df)


st.header("2) Trying streamlit widgets")

name = st.text_input("Enter your name: ")
age = st.slider("Select your age: ", 18, 50, 70)
options = ["Python", "Java", "R", "JavaScript"]
choice = st.selectbox("Choose your strongest language: ", options)

if name and age and choice:
    st.write(f"User have given name: {name} and age as: {age} with language: {choice}")



st.header("3) File uploader option")
df.to_csv('sample_data.csv', index=False)

uploaded_file = st.file_uploader("Choose a csv file: ", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

