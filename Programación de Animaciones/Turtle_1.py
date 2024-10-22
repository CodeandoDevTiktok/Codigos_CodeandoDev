import pandas as pd

# cargar archivo JSON
df = pd.read_json('archivo.json')

# transformaciones necesarias
# ...

# exportar a Excel
df.to_excel('archivo.xlsx', index=False)

