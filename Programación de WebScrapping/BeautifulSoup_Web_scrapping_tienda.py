import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# URL de búsqueda base
base_url = "https://listado.mercadolibre.com.pe"
busqueda_url = "/joyas-relojes/relojes/relojes-pulsera/relojes_NoIndex_True"

item = 1
maximo = 100

while busqueda_url and item <=maximo:
    # Realizar GET
    respuesta = requests.get(base_url + busqueda_url)
    data = BeautifulSoup(respuesta.content, "html.parser")

    # Extraer info de la página
    buscar_resultados = data.find_all("div", class_="ui-search-result__content-wrapper shops__result-content-wrapper")
    
    # Imprimir resultados de búsqueda
    for resultado in buscar_resultados:
        texto = resultado.find("h2")
        precio = resultado.find("span", class_="price-tag-text-sr-only")
        print(f"Producto {item}")
        print(f"Titulo: {texto.text.strip()}")
        print(f"Precio: {precio.text.strip()}\n")
        item +=1
    
    # Encuentra el enlace de la siguiente página
    siguiente_link = data.find("a", class_="andes-pagination__link shops__pagination-link ui-search-link")
    if siguiente_link:
        busqueda_url = urlparse(siguiente_link.get("href")).path
    else:
        busqueda_url = None
