#  Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y 
# calcule su promedio. La lectura debe detenerse al ingresar el valor -273°C

# Recopilamos la temperatura
temperatura = float(input('Ingresa la temperatura en grados Celsius: '))

# Inicializamos un contador y una suma para calcular el promedio
contador = 0
suma = 0

# Nuestro código se ejecuta hasta que el valor de temperatura sea igual a -273
while temperatura != -273:
    # La suma se actualiza sumando la temperatura a la variable suma
    suma += temperatura
    # Contamos la cantidad de valores recopilados con el contador
    contador += 1
    # Recopilamos nuevamente la temperatura
    temperatura = float(input('Ingresa la temperatura en grados Celsius: '))

promedio = suma / contador

print(f'El promedio de las temperaturas es: {promedio}')

