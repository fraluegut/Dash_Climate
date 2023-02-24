from typing import List, Dict, Tuple
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

from app import app
from utils import load_data, filter_dataframe


# Carga de datos
df = load_data()


@app.callback(
    Output(component_id='grafico_tiempo', component_property='figure'),
    Input(component_id='selector_variable', component_property='value'),
    Input(component_id='selector_fecha', component_property='start_date'),
    Input(component_id='selector_fecha', component_property='end_date'),
    Input(component_id='selector_ano', component_property='value')
)
def actualizar_grafico_tiempo(variable_seleccionada: str, fecha_inicio: str, fecha_fin: str, ano_seleccionado: List[int]) -> Dict:
    """Actualiza el gráfico de línea de tiempo con los valores de la variable seleccionada."""
    df_filtrado = filter_dataframe(df, fecha_inicio, fecha_fin, ano_seleccionado)
    fig = px.line(df_filtrado, x='fecha', y=variable_seleccionada, title=f'Variación de {variable_seleccionada} en el tiempo')
    return fig


@app.callback(
    Output(component_id='tabla_comparativa', component_property='data'),
    Input(component_id='selector_variable', component_property='value'),
    Input(component_id='selector_fecha', component_property='start_date'),
    Input(component_id='selector_fecha', component_property='end_date'),
    Input(component_id='selector_ano', component_property='value')
)
def actualizar_tabla_comparativa(variable_seleccionada: str, fecha_inicio: str, fecha_fin: str, ano_seleccionado: List[int]) -> List[Dict]:
    """Actualiza la tabla comparativa con los valores de la variable seleccionada."""
    df_filtrado = filter_dataframe(df, fecha_inicio, fecha_fin, ano_seleccionado)
    df_pivot = pd.pivot_table(df_filtrado, values=variable_seleccionada, index=['mes'], columns=['ano'])
    df_pivot.reset_index(inplace=True)
    data = df_pivot.to_dict('records')
    return data