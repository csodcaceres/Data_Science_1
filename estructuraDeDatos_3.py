#  Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: 
# [1, 4, 7, 2, 4].

# Lista que almacenará los 5 números enteros
lista_numeros = []

# Creamos un bucle que iterará 5 veces para recibir los 5 números
for i in range(0, 5):
  # Recopilamos el valor e lo insertamos en la lista 5 veces
  numero = int(input('Ingresa un número entero: '))
  lista_numeros.append(numero)
#Resultado
print(f'Lista de números ingresados: {lista_numeros}')

