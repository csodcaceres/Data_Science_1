# Podemos usar el operador de módulo % para determinar si un número es entero o decimal. 
# Si el operador de módulo % devuelve cero en la división entera de un número entre 1, 
# entonces es un número entero. De lo contrario, es un número decimal.

# Recolectamos los datos
num = float(input('Ingresa un número: '))
# Verificamos si el número es entero o decimal según el resultado del módulo
if num % 1 == 0:
    print('El número es entero.')
else:
    print('El número es decimal.')

