import xlsxwriter

libro = xlsxwriter.Workbook('ventas.xlsx')

hoja = libro.add_worksheet()

#Data

ventas = [
    {'Fecha':'2023-04-04','Producto':'Smartphone','Cantidad':3,'Precio':600},
    {'Fecha':'2023-04-05','Producto':'Smartphone','Cantidad':5,'Precio':900},
    {'Fecha':'2023-04-06','Producto':'Smartphone','Cantidad':10,'Precio':1700}
]

#Cabeceras

hoja.write('A1','Fecha')
hoja.write('B1','Producto')
hoja.write('C1','Cantidad')
hoja.write('D1','Precio')

#Registrar datos a excel

fila = 1
for venta in ventas:
    hoja.write(fila,0,venta['Fecha'])
    hoja.write(fila,1,venta['Producto'])
    hoja.write(fila,2,venta['Cantidad'])
    hoja.write(fila,3,venta['Precio'])
    fila +=1

libro.close()