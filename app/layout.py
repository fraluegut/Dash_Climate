import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

# Definir los componentes
dropdown_ano = dcc.Dropdown(
    id='dropdown-ano',
    options=[],
    value=None
)

dropdown_mes = dcc.Dropdown(
    id='dropdown-mes',
    options=[],
    value=None
)

grafico_temperaturas = dcc.Graph(
    id='grafico-temperaturas',
    figure={}
)

# Definir el layout
layout = html.Div(children=[
    html.H1(children='Datos de clima'),

    html.Div(children='''
        Seleccione los filtros:
    '''),

    html.Div(children=[
        dropdown_ano,
        dropdown_mes
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    grafico_temperaturas
])
