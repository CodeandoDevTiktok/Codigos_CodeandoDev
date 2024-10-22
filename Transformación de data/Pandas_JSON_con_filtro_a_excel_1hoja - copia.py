import pandas as pd
import requests

# Obtener el JSON de la URL
url = 'https://dummyjson.com/products'
response = requests.get(url)
data = response.json()

# Extraer los datos de la columna 'products' y normalizarlos
df = pd.json_normalize(data, 'products')

# Ordenar el DataFrame por categoría
df_sorted = df.sort_values('category')

# Obtener las categorías únicas
categorias = df_sorted['category'].unique()

ruta_salida = "salida_excel_nhojas.xlsx"
excel = pd.ExcelWriter(ruta_salida,engine="xlsxwriter")

# Iterar sobre cada categoría y guardar los datos en una hoja de Excel separada
for categoria in categorias:
    # Filtrar los datos por categoría
    datos_categoria = df_sorted[df_sorted['category'] == categoria]
    # Guardar los datos en una hoja de Excel
    datos_categoria.to_excel(excel, sheet_name=categoria, index=False)

excel.close()