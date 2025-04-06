#  Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos 
# los números primos entre 1 y el número ingresado. 
# Para este problema, necesitamos verificar si todos los números, por debajo de lo especificado 
# por el usuario, son o no divisibles por otros valores además de sí mismos. 
# Para hacer esto, podemos anidar un bucle dentro de otro. 
# Usamos un bucle para recorrer los números enteros de 2 al número ingresado. 
# Para cada número, otro bucle se utiliza para verificar si es divisible por números más pequeños 
# que él. Si el número no es divisible por ninguno de estos números, se considera un número primo. 
# Esta estructura se puede observar a continuación:

# Recopilamos el número
numero = int(input('Ingresa un número entero: '))
# Lista para almacenar los números primos
lista_primos = []
# Bucle que recorre todos los números por debajo del número ingresado
for num in range(2, numero):
  # Primo es una bandera que nos permite saber si el valor analizado es primo o no.
  primo = True
  # Probamos si todos los números por debajo del especificado en el primer bucle pueden dar una división exacta.
  for prueba_divisibles in range(2, num):
    if num % prueba_divisibles == 0:
      # Si es divisible por algún número, entendemos que el número no es primo y terminamos el bucle interno con break.
      primo = False
      break
  # La condición se convierte en el resultado booleano de primo: False. Ignoramos la condición True y ejecutamos el bloque del if.
  if primo:
    lista_primos.append(num)
# Resultado
print(f'Lista de números primos: {lista_primos}')

