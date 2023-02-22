import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from datetime import date, timedelta
import random

# Creamos una tabla con datos de ejemplo
# df = pd.DataFrame({
#     'fecha': pd.date_range(start='2022-01-01', end='2022-02-28'),
#     'temperatura': np.random.randint(0, 40, size=(59)),
#     'humedad': np.random.randint(0, 100, size=(59))
# })
def generar_datos_clima(ciudad, anios=5):
    # Definir las fechas
    hoy = date.today()
    fechas = [hoy - timedelta(days=x) for x in range(365*anios)]

    # Generar los datos aleatorios
    temperaturas = [round(random.uniform(10, 30), 1) for _ in range(len(fechas))]
    humedades = [round(random.uniform(30, 90), 1) for _ in range(len(fechas))]

    # Crear el dataframe
    df = pd.DataFrame({'ciudad': ciudad,
                       'fecha': fechas,
                       'temperatura': temperaturas,
                       'humedad': humedades})
    return df

df = generar_datos_clima('Ciudad de México', anios=3)
df['fecha'] = pd.to_datetime(df['fecha'])
# Creamos la aplicación de Dash
app = dash.Dash(__name__)

# Creamos el diseño de la aplicación
app.layout = html.Div([
    html.H1('Dashboard del Clima'),
    dcc.Dropdown(
        id='seleccionar-ciudad',
        options=[
            {'label': 'Ciudad 1', 'value': 'ciudad1'},
            {'label': 'Ciudad 2', 'value': 'ciudad2'},
            {'label': 'Ciudad 3', 'value': 'ciudad3'}
        ],
        value='ciudad1'
    ),
    dcc.DatePickerRange(
        id='filtro-fechas',
        min_date_allowed=df['fecha'].min(),
        max_date_allowed=df['fecha'].max(),
        start_date=df['fecha'].min(),
        end_date=df['fecha'].max()
    ),
    dcc.Dropdown(
        id='selector-ano',
        options=[{'label': str(ano), 'value': ano} for ano in df['fecha'].dt.year.unique()],
        value=df['fecha'].dt.year.max()
    ),
    dcc.Graph(id='grafico-clima')
])


# Creamos una función que actualice el gráfico según la ciudad seleccionada, el rango de fechas y el año de comparación
@app.callback(
    dash.dependencies.Output('grafico-clima', 'figure'),
    [dash.dependencies.Input('seleccionar-ciudad', 'value'),
     dash.dependencies.Input('filtro-fechas', 'start_date'),
     dash.dependencies.Input('filtro-fechas', 'end_date'),
     dash.dependencies.Input('selector-ano', 'value')]
)
def actualizar_grafico(ciudad_seleccionada, start_date, end_date, ano_seleccionado):
    # Filtramos los datos según la ciudad seleccionada y el rango de fechas
    if ciudad_seleccionada == 'ciudad1':
        df_ciudad = df
    elif ciudad_seleccionada == 'ciudad2':
        df_ciudad = df + 5
    else:
        df_ciudad = df - 5

    df_filtrado = df_ciudad[(df_ciudad['fecha'] >= start_date) & (df_ciudad['fecha'] <= end_date)]

    # Filtramos los datos según el año seleccionado
    df_ano_seleccionado = df_ciudad[df_ciudad['fecha'].dt.year == ano_seleccionado]
    df_filtrado_ano = df_ano_seleccionado[
        (df_ano_seleccionado['fecha'] >= start_date) & (df_ano_seleccionado['fecha'] <= end_date)]

    # Creamos el gráfico
    grafico = go.Figure()
    grafico.add_trace(go.Scatter(x=df_filtrado['fecha'], y=df_filtrado['temperatura'], mode='lines',
                                 name='Temperatura'))
    grafico.add_trace(go.Scatter(x=df_filtrado_ano['fecha'], y=df_filtrado_ano['temperatura'],
                                 mode='lines',
                                 name=f'Temperatura {ano_seleccionado}'))
    grafico.add_trace(go.Scatter(x=df_filtrado['fecha'], y=df_filtrado['humedad'],
                                 mode='lines',
                                 name='Humedad'))
    grafico.add_trace(go.Scatter(x=df_filtrado_ano['fecha'], y=df_filtrado_ano['humedad'],
                                 mode='lines',
                                 name=f'Humedad {ano_seleccionado}'))
    grafico.update_layout(title='Datos del Clima',
                          xaxis_title='Fecha',
                          yaxis_title='Valor')
    return grafico

# Iniciamos el servidor de la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)