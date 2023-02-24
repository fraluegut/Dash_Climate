import pandas as pd


def load_data() -> pd.DataFrame:
    """Carga los datos de ejemplo."""
    df = pd.DataFrame({
        'fecha': pd.date_range(start='2020-01-01', end='2023-12-31', freq='D'),
        'ano': [d.year for d in pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')],
        'mes': [d.month for d in pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')],
        'temperatura': [20.1, 21.5, 22.6, 18.9] * 365,
        'humedad': [60, 65, 70, 75] * 365
    })
    return df


import pandas as pd


def filter_dataframe(df, start_date, end_date, years):
    """
    Función auxiliar para filtrar el dataframe según los valores seleccionados por el usuario.

    Args:
        df (pd.DataFrame): DataFrame que se va a filtrar.
        start_date (str): Fecha de inicio del rango seleccionado por el usuario.
        end_date (str): Fecha de fin del rango seleccionado por el usuario.
        years (list): Lista de años seleccionados por el usuario.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    # Filtrar el dataframe por el rango de fechas seleccionado
    mask = (df['fecha'] >= pd.to_datetime(start_date)) & (df['fecha'] <= pd.to_datetime(end_date))
    df = df.loc[mask]

    # Filtrar el dataframe por los años seleccionados
    if years:
        df = df[df['fecha'].dt.year.isin(years)]

    return df
