import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

url = 'https://fbref.com/es/comps/8/Estadisticas-de-Champions-League'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encuentra todas las tablas de estadísticas
tablas = soup.find_all('table')

# Crea un libro de Excel
libro = Workbook()

# Itera sobre las tablas
for i, tabla in enumerate(tablas):
    filas = tabla.find_all('tr')

    # Encabezados de columna
    encabezados = [th.get_text() for th in filas[0].find_all(['th', 'td'])]
    print(f"Tabla {i+1} - Encabezados: {len(encabezados)}")

    # Itera sobre las filas y extrae los datos
    datos = []
    for fila in filas[1:]:
        fila_datos = [td.get_text() for td in fila.find_all(['th', 'td'])]
        if len(fila_datos) == len(encabezados):
            datos.append(fila_datos)
    print(f"Tabla {i+1} - Datos: {len(datos)} filas")
    
    # Crea un DataFrame de pandas con los encabezados y datos
    df = pd.DataFrame(datos, columns=encabezados)

    # Crea una hoja en el libro de Excel
    hoja = libro.create_sheet(title=f'Tabla {i+1}')

    # Escribe los encabezados en la hoja
    hoja.append(encabezados)

    # Escribe los valores de la tabla en la hoja
    for fila in df.values:
        hoja.append(fila.tolist())

# Elimina la hoja de inicio predeterminada
libro.remove(libro['Sheet'])

# Guarda el libro de Excel
nombre_archivo = 'tablas_champions.xlsx'
libro.save(nombre_archivo)
print(f"Tablas exportadas a {nombre_archivo}")