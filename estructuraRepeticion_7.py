# Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y 
# seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. 
# Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.

# Recopilamos el número
num = int(input('Ingresa un número entero: '))

# Los números enteros iguales o menores que 1 no se consideran primos
if num > 1:
    for i in range(2, num):
        # Verificamos todos los residuos de la división entre todos los números menores que num
        # Si algún residuo es 0, significa que es divisible por otro número además de sí mismo y 1
        if (num % i) == 0:
            print(f'{num} no es un número primo')
            break
    else:
        print(f'{num} es un número primo')
else:
    print(f'{num} no es un número primo')

