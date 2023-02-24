import random
import csv
from datetime import datetime, timedelta

# Definimos la fecha inicial y final
fecha_inicial = datetime(2021, 1, 1, 0, 0, 0)  # Inicial: 1 de enero de 2022 a las 00:00:00
fecha_final = datetime(2022, 2, 1, 0, 0, 0)  # Final: 1 de febrero de 2022 a las 00:00:00

# Definimos las variables a generar
variables = ['hora', 'fecha', 'temperatura', 'humedad', 'presion', 'lluvia']

# Abrimos el archivo csv en modo escritura
with open('datos.csv', mode='w', newline='') as archivo_csv:
    # Creamos el objeto escritor csv
    writer = csv.DictWriter(archivo_csv, fieldnames=variables)
    # Escribimos la primera fila con los nombres de las columnas
    writer.writeheader()

    # Generamos los registros por hora
    delta = timedelta(hours=1)
    fecha_actual = fecha_inicial
    while fecha_actual < fecha_final:
        # Generamos valores aleatorios para las variables
        hora = fecha_actual.strftime('%H:%M:%S')
        fecha = fecha_actual.strftime('%Y-%m-%d')
        temperatura = round(random.uniform(10, 30), 2)
        humedad = round(random.uniform(20, 90), 2)
        presion = round(random.uniform(900, 1100), 2)
        lluvia = round(random.uniform(0, 10), 2)

        # Escribimos el registro en el archivo csv
        writer.writerow(
            {'hora': hora, 'fecha': fecha, 'temperatura': temperatura, 'humedad': humedad, 'presion': presion,
             'lluvia': lluvia})

        # Avanzamos a la siguiente hora
        fecha_actual += delta
