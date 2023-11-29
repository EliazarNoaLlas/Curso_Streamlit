import streamlit as st
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Iniciar la aplicación Dash dentro de Streamlit
dash_app = dash.Dash(__name__, server=st._Server)

# Conjunto de datos inicial
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Diseño del formulario en Dash
form_layout = html.Div([
    html.H3("Modificar Nombres de Columnas"),
    dcc.Input(id='col_a', type='text', placeholder='Nuevo nombre para A'),
    dcc.Input(id='col_b', type='text', placeholder='Nuevo nombre para B'),
    dcc.Input(id='col_c', type='text', placeholder='Nuevo nombre para C'),
    html.Button('Aceptar', id='submit-button', n_clicks=0)
])

# Diseño del gráfico en Dash
graph_layout = html.Div([
    dcc.Graph(id='scatter-plot')
])

# Diseño principal de la aplicación Dash
dash_app.layout = html.Div([
    html.Div([form_layout], style={'width': '30%', 'float': 'left'}),
    html.Div([graph_layout], style={'width': '70%', 'float': 'right'})
])

# Callback para actualizar el conjunto de datos en tiempo real
@dash_app.callback(
    Output('scatter-plot', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('col_a', 'value'),
     dash.dependencies.State('col_b', 'value'),
     dash.dependencies.State('col_c', 'value')]
)
def update_dataset(n_clicks, new_col_a, new_col_b, new_col_c):
    if n_clicks > 0:
        # Actualizar los nombres de las columnas según el formulario
        df.columns = [new_col_a, new_col_b, new_col_c]

    # Crear un gráfico de dispersión con el conjunto de datos actualizado
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="Scatter Plot")
    return fig

# Convertir la aplicación Dash en un componente de Streamlit
st_dash_component = st.components.v1.html(dash_app.to_html(), height=700)

# Mostrar el componente de Streamlit
st.components.v1.html(st_dash_component, height=700)

