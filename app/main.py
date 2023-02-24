import plotly.express as px
import dash
from dash import html, dcc
import pandas as pd

# Cargar los datos del archivo csv
# df = pd.read_csv('datos_clima.csv')
df = pd.read_csv('data.csv')
# Definir el estilo
external_stylesheets = ['style.css']
#
# # Crear la aplicación Dash
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# # Definir el layout de la aplicación
# app.layout = html.Div(children=[
#     html.H1(children='Dashboard'),
#
#     # Definir las pestañas
#     dcc.Tabs(id="tabs", children=[
#         # Primera pestaña
#         dcc.Tab(label='Pestaña 1', children=[
#             html.Div(children=[
#                 html.Label('Selecciona el periodo:'),
#                 dcc.DatePickerRange(
#                     id='date-range',
#                     min_date_allowed=df['fecha'].min(),
#                     max_date_allowed=df['fecha'].max(),
#                     start_date=df['fecha'].min(),
#                     end_date=df['fecha'].max()
#                 ),
#                 html.Label('Selecciona las variables:'),
#                 dcc.Checklist(
#                     id='variables',
#                     options=[
#                         {'label': 'Temperatura', 'value': 'temperatura'},
#                         {'label': 'Humedad', 'value': 'humedad'},
#                         {'label': 'Agua acumulada', 'value': 'agua acumulada'},
#                         {'label': 'Luz', 'value': 'luz'},
#                         {'label': 'Presión', 'value': 'presión'}
#                     ],
#                     value=['temperatura', 'humedad']
#                 ),
#                 html.Label('Selecciona la media:'),
#                 dcc.RadioItems(
#                     id='media',
#                     options=[
#                         {'label': 'Media', 'value': 'mean'},
#                         {'label': 'Máximo', 'value': 'max'},
#                         {'label': 'Mínimo', 'value': 'min'}
#                     ],
#                     value='mean'
#                 ),
#                 dcc.Graph(id='graph')
#             ])
#         ]),
#
#         # Segunda pestaña
#         dcc.Tab(label='Pestaña 2', children=[
#             html.Div(children=[
#                 html.Label('Selecciona las variables:'),
#                 dcc.Checklist(
#                     id='variables2',
#                     options=[
#                         {'label': 'Temperatura', 'value': 'temperatura'},
#                         {'label': 'Humedad', 'value': 'humedad'},
#                         {'label': 'Agua acumulada', 'value': 'agua acumulada'},
#                         {'label': 'Luz', 'value': 'luz'},
#                         {'label': 'Presión', 'value': 'presión'}
#                     ],
#                     value=['temperatura', 'humedad']
#                 ),
#                 html.Label('Selecciona los años a comparar:'),
#                 dcc.Dropdown(
#                     id='years',
#                     options=[{'label': '2021', 'value': 2021},
#                              {'label': '2022', 'value': 2022}],
#                     multi=True,
#                     value=[2021, 2022]
#                 ),
#                 dcc.Graph(id='graph2')
#             ])
#         ])
#     ])
# ])
#
#
# # Definir las funciones para actualizar las gráficas
# @app.callback(
#     dash.dependencies.Output('graph', 'figure'),
#     [dash.dependencies.Input('date-range', 'start_date'),
#      dash.dependencies.Input('date-range', 'end_date'),
#      dash.dependencies.Input('variables', 'value'),
#      dash.dependencies.Input('media', 'value')])
# def update_graph(start_date, end_date, variables, media):
#     filtered_df = df[(df['fecha'] >= start_date) & (df['fecha'] <= end_date)]
#     traces = []
#     for variable in variables:
#         traces.append(
#             {'x': filtered_df['fecha'], 'y': filtered_df[variable].rolling('7d', center=True).apply(media).values,
#              'name': variable})
#     return {'data': traces, 'layout': {'title': 'Gráfica dinámica'}}
#
#
# @app.callback(
#     dash.dependencies.Output('graph2', 'figure'),
#     [dash.dependencies.Input('variables2', 'value'),
#      dash.dependencies.Input('years', 'value')])
# def update_graph2(variables, years):
#     traces = []
#     for year in years:
#         filtered_df = df[df['fecha'].dt.year == year]
#         for variable in variables:
#             traces.append({'x': filtered_df['fecha'], 'y': filtered_df[variable], 'name': f'{variable} - {year}'})
#     return {'data': traces, 'layout': {'title': 'Comparación de años'}}
#
#
# # Ejecutar la aplicación
# if __name__ == '__main__':
#     app.run_server(debug=True)


# Crear la gráfica utilizando Plotly
fig = px.line(df, x='Fecha', y='Temperatura')

# Definir la aplicación Dash y su diseño
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='temperatura-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)