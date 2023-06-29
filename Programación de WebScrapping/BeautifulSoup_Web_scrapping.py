import requests
from bs4 import BeautifulSoup

#obtener contenido HTML

web = "https://es.wikipedia.org/wiki/Python"

respuesta = requests.get(web)

respuesta_html = respuesta.text

#Analiza contenido HTMl

contenido = BeautifulSoup(respuesta_html,"html.parser")

#Extrae informacion

titulo = contenido.find("h1",id="firstHeading").text

parrafos = contenido.find_all("p")

#Imprimir informacion

print("titulo: ", titulo)
print("primeros parrafos")
for i in range (3):
    print(parrafos[i].text)