# Podemos usar el operador de módulo % para determinar si un número es par o impar. 
# Si la división entera de un número entre 2 da como resultado 0, entonces es par. 
# Si no, es impar. Esto se debe a que todos los números pares son divisibles por 2, 
# por lo que no tienen un residuo en la división.

# Recolectamos los datos
num = int(input('Ingresa un número: '))

# Verificamos si el número es par según el resultado del módulo
if num % 2 == 0:
    print('El número es par.')
else:
    print('El número es impar.')

