"""
IDE: replit.com
Ruta 2024 Python:
Videos grabados en Kick: 
SEGUIR: https://kick.com/codeando

2. Operadores: La Base del Cálculo en Programación
"""
#Operadores Aritméticos
# + - * / // % **

#Operador de asignacion
# =

precio_unitario = 101
costo_unitario = 76
cantidad_tienda_peru = 66
cantidad_tienda_mexico = 83
socios = 7
socio_1 = "Jorge"
socio_2 = 'Zenaida'
socio_3 = "jorge"

cantidad_total = cantidad_tienda_peru + cantidad_tienda_mexico
ganancia_unitaria = precio_unitario - costo_unitario
ganancia_total = ganancia_unitaria * cantidad_total
ganancia_por_socio = ganancia_total / socios
ganancia_por_socio_exacta = ganancia_total // socios
ejemplo_modulo = ganancia_total % socios
ejemplo_exponente = socios**2

#Operadores de comparacion
# == != > < >= <=

comparacion_1 = ganancia_por_socio == ganancia_por_socio_exacta
comparacion_2 = ganancia_por_socio != ganancia_por_socio_exacta
comparacion_3 = ganancia_por_socio > ganancia_por_socio_exacta
comparacion_4 = ganancia_por_socio < ganancia_por_socio_exacta
comparacion_5 = ganancia_por_socio >= ganancia_por_socio_exacta
comparacion_6 = ganancia_por_socio <= ganancia_por_socio_exacta
comparacion_7 = socio_1 == socio_3
comparacion_8 = socio_1 != socio_3
comparacion_9 = socio_1 > socio_2

#Operadores Logicos
# and(Y) or(O) not(NEGACION)

comparacion_10 = (cantidad_total > cantidad_tienda_peru
                  and cantidad_total < cantidad_tienda_mexico)
comparacion_11 = (cantidad_total > cantidad_tienda_peru
                  or cantidad_total < cantidad_tienda_mexico)
comparacion_12 = not cantidad_total > cantidad_tienda_peru

#Operadores de inclusion
# in(ESTA DENTRO) not in(NO ESTA DENTRO)

#Operadores incrementales
# += -= *= /= //= %= **=

numero = 0
numero += 5
numero = numero + 5
