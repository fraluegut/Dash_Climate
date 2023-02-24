import dash
from dash import html, dcc
import pandas as pd
from datetime import datetime as dt
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Cargar los datos
df = pd.read_csv('datos.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

# Crear la aplicación
app = dash.Dash(__name__)

# Definir las opciones del menú desplegable
variable_options = [{'label': 'Temperatura', 'value': 'temperatura'},
                    {'label': 'Humedad', 'value': 'humedad'},
                    {'label': 'Presión', 'value': 'presion'},
                    {'label': 'Lluvia', 'value': 'lluvia'}]

# Definir la página principal
app.layout = html.Div([
    # Título de la página
    html.H1('Dashboard'),

    # Menú desplegable para seleccionar la variable
    dcc.Dropdown(id='variable-selector', options=variable_options, value='temperatura'),

    # Seleccionador de fecha inicial y final
    dcc.DatePickerRange(
        id='date-range-picker',
        min_date_allowed=df['fecha'].min(),
        max_date_allowed=df['fecha'].max(),
        start_date=df['fecha'].min(),
        end_date=df['fecha'].max()
    ),

    # Gráfica de la variable seleccionada
    dcc.Graph(id='variable-graph')
])


# Definir las funciones para actualizar las gráficas
@app.callback(Output('variable-graph', 'figure'),
              [Input('variable-selector', 'value'),
               Input('date-range-picker', 'start_date'),
               Input('date-range-picker', 'end_date')])
def update_variable_graph(variable, start_date, end_date):
    # Convertir las fechas en objetos datetime
    start_date = dt.strptime(start_date[:10], '%Y-%m-%d')
    end_date = dt.strptime(end_date[:10], '%Y-%m-%d')

    # Filtrar los datos por rango de fechas
    filtered_df = df[(df['fecha'] >= start_date) & (df['fecha'] <= end_date)]

    # Obtener los datos de la variable seleccionada
    y = filtered_df[variable]

    # Crear la figura de la gráfica
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['fecha'], y=y, mode='lines'))
    fig.update_layout(title=f'{variable.capitalize()} vs. fecha', xaxis_title='fecha',
                      yaxis_title=variable.capitalize())

    return fig


# Iniciar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
