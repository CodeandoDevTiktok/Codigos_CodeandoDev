import requests
from bs4 import BeautifulSoup

# URL de búsqueda base
base_url = "https://es.wikipedia.org"
busqueda_url = "/w/index.php?fulltext=1&search=python&title=Especial:Buscar&ns0=1&ns100=1&ns104=1"
numero=0


while busqueda_url:
    # Realizar GET
    respuesta = requests.get(base_url + busqueda_url)
    data = BeautifulSoup(respuesta.content, "html.parser")
    
    # Extraer  info de la página
    buscar_resultados = data.find_all("div", class_="mw-search-result-heading")

    # Imprimir resultados de búsqueda
    
    for resultado in buscar_resultados:
        link = resultado.find("a")
        print(f"Resultado {numero+1}:")
        print(f"Title: {link.text.strip()}")
        print(f"Link: {base_url}{link['href']}\n")
        numero+=1

    # Encuentra el enlace de la siguiente página
    siguiente_link = data.find("a", string="20 siguientes")
    if siguiente_link:
        busqueda_url = siguiente_link.get("href")
    else:
        busqueda_url = None