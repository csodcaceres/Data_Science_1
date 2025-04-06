# Escribe un programa que solicite dos números enteros e imprima todos los números enteros 
# entre ellos.

# Recolectamos los valores de inicio y fin
inicio = int(input('Ingresa el primer número entero: '))
fin = int(input('Ingresa el segundo número entero: '))

# Verificamos si el valor de inicio es menor que el fin
if inicio < fin:
  # Podemos imprimir los enteros entre el valor menor y el valor mayor
  for i in range(inicio + 1, fin):
    print(i)
elif inicio > fin:
  for i in range(fin + 1, inicio):
    print(i)
else: # En caso de que los números sean iguales, no podemos imprimir ninguna secuencia.
  print('Los números son iguales.')

