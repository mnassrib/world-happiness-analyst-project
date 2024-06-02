import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://flask_api:5000/happiness"

st.title("World Happiness Report 2024")

@st.cache_data
def load_data():
    response = requests.get(API_URL)
    data = response.json()
    return pd.DataFrame(data)

df = load_data()
available_columns = [col for col in df.columns if col not in ["country", "year"]]

st.write("## Data Overview")
st.write(df.head())

st.write("## Happiness Score by Country")

# Utilisation des colonnes de disposition pour afficher les éléments côte à côte
country, variable_y = st.columns(2)

with country:
    selected_country = st.selectbox('Select a country:', df['country'].unique())

with variable_y:
    selected_variable_y = st.selectbox('Select Y-axis variable:', available_columns)

data_country = df[df['country'] == selected_country]

# Replace underscores with spaces in the selected Y-axis variable
variable_y_label = selected_variable_y.replace('_', ' ').title()

# Créez le graphique en ligne avec Plotly
fig = px.line(
    data_country, 
    x='year', 
    y=selected_variable_y, 
    title=f'Happiness score explained by {variable_y_label} over year for {selected_country}',
    labels={
        'year': 'Year',
        selected_variable_y: variable_y_label
    }
)

# Affichez le graphique dans Streamlit
st.plotly_chart(fig)
