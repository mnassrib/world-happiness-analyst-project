import streamlit as st
import requests
import pandas as pd

API_URL = "http://flask_api:5000/happiness"

st.title("World Happiness Report")

@st.cache_data
def load_data():
    response = requests.get(API_URL)
    data = response.json()
    return pd.DataFrame(data)

df = load_data()

st.write("## Data Overview")
st.write(df.head())

st.write("## Happiness Score by Country")
country = st.selectbox('Select a country:', df['country'].unique())
data_country = df[df['country'] == country]
st.line_chart(data_country[['year', 'happiness_score']].set_index('year'))
