
#NO hay elementos duplicados
animales = {"perro", "gato", "leon", "tigre"}

colores = {"rojo", "verde", "azul"}

numeros_pares = {2, 4, 14, 28}
numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}

resultado = numeros_pares.union(numeros)
print(resultado)

resultado_2 = numeros_pares.intersection(numeros)
print(resultado_2)

print("conjunto inicial:", numeros_pares)
numeros_pares.pop()
print("pop:", numeros_pares)
numeros_pares.remove(14)
print("remove 14", numeros_pares)

for numero in resultado:
  print(numero)