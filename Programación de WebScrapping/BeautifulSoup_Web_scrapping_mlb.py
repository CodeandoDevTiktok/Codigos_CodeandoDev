import datetime
import requests
from bs4 import BeautifulSoup

# URL de búsqueda base
base_url = "https://www.mlb.com/scores/"

# Obtener la fecha de hoy
fecha_actual = datetime.date.today()

item = 1
maximo = 10

while item <= maximo:
    # Obtener la fecha de búsqueda
    fecha_busqueda = fecha_actual - datetime.timedelta(days=item-1)
    busqueda_url = fecha_busqueda.strftime("%Y-%m-%d")
    
    # Realizar GET
    url_completa = base_url + busqueda_url
    respuesta = requests.get(url_completa)
    data = BeautifulSoup(respuesta.content, "html.parser")
    
    # Extraer info de la página
    buscar_resultados = data.find_all("div", class_="grid-itemstyle__GridItemWrapper-sc-cq9wv2-0 gmoPjI")

    for resultado in buscar_resultados:
        texto = resultado.find("div", class_="StatusLayerstyle__StatusLayerWrapper-sc-1s2c2o8-1 jkfZwE")
        #print(texto)
        equipos = resultado.find_all("div", class_="TeamWrappersstyle__DesktopTeamWrapper-sc-uqs6qh-0 fdaoCu")
        puntajes = resultado.find_all("td", class_="table-cellstyle__StyledTableCell-sc-xpntj7-2 ljCIPI")
        if texto is not None:
            # Imprimir resultados de búsqueda
            print(f"Fecha: {busqueda_url}")
            print(f"Título: {texto.text.strip()}")
            if len(equipos) >= 2 and len(puntajes) >= 6:
                equipo1 = equipos[0]
                equipo2 = equipos[1]
                print(f"Equipo 1: {equipo1.text.strip()} - R: {puntajes[0].text.strip()} - H: {puntajes[1].text.strip()} - E: {puntajes[2].text.strip()}")
                print(f"Equipo 2: {equipo2.text.strip()} - R: {puntajes[3].text.strip()} - H: {puntajes[4].text.strip()} - E: {puntajes[5].text.strip()}\n")
            else:
                print("No se encontraron suficientes equipos\n")
        else:
            print("Texto no encontrado\n")
    
    item += 1