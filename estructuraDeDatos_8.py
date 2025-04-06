# Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados 
# por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar 
# son amargos. 
# Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y 
# amargos.

# Lista que contendrá los valores de IDs
ids = []
# Variables contadoras de dulces y amargos
dulce = 0
amargo = 0

# Creamos un bucle que iterará 10 veces para recopilar los 10 IDs
for i in range(0,10):
  # Recopilamos el ID y lo agregamos a la lista
  ids.append(int(input(f'Ingrese el ID {i+1}°: ')))

# Leemos todos los elementos de la lista de IDs y los asignamos a id
for id in ids:
  # Verificamos si los elementos son pares o impares para llevar el conteo
  if id % 2 == 0:
    dulce += 1
  else:
    amargo += 1

# Resultado
print(f'Cantidad de productos dulces: {dulce}')
print(f'Cantidad de productos amargos: {amargo}')
