import pandas as pd
import requests

# Obtener el JSON de la URL
url = '3'
respuesta = requests.get(url)
data = respuesta.json()

# Extraer los datos de la columna 'products' y normalizarlos
dataframe = pd.json_normalize(data, 'products')

# Ordenar el DataFrame por categoría
ordena_dataframe = dataframe.sort_values('category')

# Crear un objeto ExcelWriter para guardar los datos en un archivo de Excel
ruta_salida = "salida_excel_1hoja.xlsx"
excel = pd.ExcelWriter(ruta_salida, engine="xlsxwriter")

# Obtener las categorías únicas
categorias = ordena_dataframe['category'].unique()

# Especificar la fila de inicio
inicia_fila = 0

# Iterar sobre cada categoría y copiar los datos en la misma hoja de Excel
for categoria in categorias:
    # Filtrar los datos por categoría
    datos_categoria = ordena_dataframe[ordena_dataframe['category'] == categoria]
    
    # Copiar los datos en la hoja de Excel
    datos_categoria.to_excel(excel, sheet_name='Tablas', startrow=inicia_fila, index=False)
    
    # Actualizar la fila de inicio para la siguiente categoría
    inicia_fila += len(datos_categoria) + 2  # Agregar un espacio entre las tablas

excel.close()
