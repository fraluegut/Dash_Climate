import pandas as pd

def load_data():
    # Cargar los datos
    df = pd.read_csv('datos_clima.csv')

    # Procesar los datos
    df['fecha'] = pd.to_datetime(df['fecha'])

    return df
