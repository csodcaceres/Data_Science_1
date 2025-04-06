# Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado. 
# Dado que el objetivo es imprimir la lista de números enteros en orden inverso al ingresado, 
# podemos utilizar la técnica de partición, en la que la lista se recorre desde el último elemento 
# (usando el índice -1) hasta el primero. De esta manera, la lista se imprime en orden inverso 
# al original, de modo que el último elemento es el primero en mostrarse, seguido por el penúltimo 
# elemento y así sucesivamente.

# Lista que almacenará los 5 números enteros
lista_numeros = []

# Creamos un bucle que iterará 5 veces para recibir los 5 números
for i in range(0, 5):
  # Recopilamos el valor e lo insertamos en la lista 5 veces
  numero = int(input('Ingresa un número entero: '))
  lista_numeros.append(numero)
# Usamos la técnica de partición para imprimir el resultado
print(f'Lista de números invertida: {lista_numeros[::-1]}')

