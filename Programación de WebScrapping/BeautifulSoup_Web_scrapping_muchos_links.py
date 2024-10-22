import requests
from bs4 import BeautifulSoup

# URL de Wikipedia
url = "https://es.wikipedia.org/wiki/OpenAI"

# solicitud GET
response = requests.get(url)

# Crea objeto BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar todos los enlaces
enlaces = soup.find_all("a")

# Recorrer los enlaces y extraer su texto y URL
for enlace in enlaces:
    texto = enlace.text
    url_enlace = enlace["href"]
    
    # Si el enlace comienza con "/wiki/", es un enlace interno de Wikipedia
    if url_enlace.startswith("/wiki/"):
        # Crear la URL completa del enlace interno
        url_completa = "https://es.wikipedia.org" + url_enlace
        print("Texto: ", texto)
        print("URL: ", url_completa)
        print("------------------------------------")
