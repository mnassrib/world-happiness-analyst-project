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
    # Appliquer replace('_', ' ').title() sur chaque élément de available_columns
    formatted_columns = [column.replace('_', ' ').title() for column in available_columns]
    variable_y_label = st.selectbox('Select Y-axis variable:', formatted_columns)

data_country = df[df['country'] == selected_country]

# Créez le graphique en ligne avec Plotly
fig = px.line(
    data_country, 
    x='year', 
    y=variable_y_label.replace(' ', '_').lower(), 
    title=f'Happiness score explained by {variable_y_label} over year for {selected_country}',
    labels={
        'year': 'Year',
        variable_y_label.replace(' ', '_').lower(): variable_y_label
    }
)

# Affichez le graphique dans Streamlit
st.plotly_chart(fig)

st.write("## Compare Countries")

countries = st.multiselect('Select countries:', df['country'].unique())
variable = st.selectbox('Select variable:', available_columns)

if len(countries) > 0:
    data_countries = df[df['country'].isin(countries)]

    fig = px.line(
        data_countries, 
        x='year', 
        y=variable, 
        color='country', 
        title=f'Comparison of {variable} over the years for selected countries',
        labels={
            'year': 'Year',
            variable: variable.replace('_', ' ').title()
        }
    )

    st.plotly_chart(fig)
