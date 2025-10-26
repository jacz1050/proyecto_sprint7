import pandas as pd
import plotly.express as px
import streamlit as st

# Prueba con pandas
df = pd.DataFrame({
    "Ciudad": ["CDMX", "Guadalajara", "Monterrey"],
    "Población": [9200000, 1500000, 1100000]
})

# Prueba con plotly
fig = px.bar(df, x="Ciudad", y="Población", title="Población por ciudad")

# Prueba con streamlit
st.title("✅ Test de librerías")
st.write("Si ves esto, pandas, plotly y streamlit funcionan correctamente")
st.plotly_chart(fig)