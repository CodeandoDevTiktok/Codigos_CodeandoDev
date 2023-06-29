from bs4 import BeautifulSoup
import requests

# URL de Wikipedia 
url = 'https://es.wikipedia.org/wiki/Python'

# Obten contenido HTML
response = requests.get(url)
html_content = response.content

# Crear un objeto Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Impresiones en terminal

print("=== INFORME DE ANÁLISIS DEL HTML ===")
print("\n=== Estructura del HTML ===")
print(soup.prettify())
print("\n=== Patrones Comunes ===")

# Enlaces
enlaces = soup.find_all('a')
print("Número de enlaces:", len(enlaces))

# Títulos
titulos = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print("Número de títulos:", len(titulos))

# Imágenes
imagenes = soup.find_all('img')
print("Número de imágenes:", len(imagenes))

# Tablas
tablas = soup.find_all('table')
print("Número de tablas:", len(tablas))

# Listas
listas = soup.find_all(['ul', 'ol'])
print("Número de listas:", len(listas))
