import requests
import openpyxl

# Hacer la petición GET al JSON
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Convertir la respuesta a un diccionario de Python
data = response.json()

# Crear un nuevo libro de Excel
libro = openpyxl.Workbook()

# Seleccionar la hoja activa
hoja = libro.active

# Escribir los datos en la hoja
hoja.append(['User ID', 'ID', 'Title', 'Body'])
for post in data:
    hoja.append([post['userId'], post['id'], post['title'], post['body']])

# Ajustar el ancho de las columnas automáticamente
for columna in hoja.columns:
    length = max(len(str(cell.value)) for cell in columna)
    hoja.column_dimensions[columna[0].column_letter].width = length + 2

# Guardar el libro de Excel
libro.save('posts.xlsx')
