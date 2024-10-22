import pandas
import pymysql

#Conexion a la BD MySQL

conexion = pymysql.connect(host="localhost",
                           user="root",
                           password="root")

#Crear BD

with conexion.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS base_fin;")
    
#Conexion con BD

conexion.select_db("base_fin")

#Leer Excel

excel_data = pandas.read_excel("data_excel_a_mysql.xlsx")

#Obtener columnas

columnas = excel_data.columns.tolist()

#Crear consulta SQL

crear_tabla_query = f"CREATE TABLE tabla ({','.join([f'`{col}` VARCHAR(255)' for col in columnas])});"

#Ejecutar consulta

with conexion.cursor() as cursor:
    cursor.execute(crear_tabla_query)

#Insertar data a tabla MySQL

with conexion.cursor() as cursor:
    for _,fila in excel_data.iterrows():
        insertar_fila_query = "INSERT INTO tabla VALUES ({});".format(','.join([f"'{valor}'" for valor in fila]))
        cursor.execute(insertar_fila_query)

#Confirmar cambios

conexion.commit()
conexion.close()
    