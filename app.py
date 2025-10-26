import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis interactivo de anuncios de vehículos 🚗')

show_hist = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión: Precio vs Kilometraje')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Kilometraje (odometer)',
        yaxis_title='Frecuencia',
        template='plotly_white'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs Kilometraje')
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(color='royalblue', opacity=0.6),
        name='Vehículos'
    )])
    fig_scatter.update_layout(
        title_text='Precio vs Kilometraje',
        xaxis_title='Kilometraje (odometer)',
        yaxis_title='Precio (USD)',
        template='plotly_white'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)