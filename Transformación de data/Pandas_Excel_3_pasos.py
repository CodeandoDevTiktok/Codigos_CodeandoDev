import pandas as pd

data = [
    {"Nombre": "Mario Bros", "Año":1985, "Plataforma": "NES"},
    {"Nombre": "The Legend of Zelda", "Año":1986, "Plataforma": "NES"},
    {"Nombre": "Minecraft", "Año":2011, "Plataforma": "Varios"}
]

dataExcel = pd.DataFrame(data)

dataExcel.to_excel("juegos.xlsx")
