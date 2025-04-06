# Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. 
# Recuerda que el factorial de un número entero es el producto de ese número por todos sus 
# antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.

# Solicita el número
num = int(input('Ingresa un número entero: '))

# Inicializa el cálculo
factorial = 1

# Nuestro contador comienza con el número máximo
# y se realizará un conteo decreciente con el operador -=
i = num
while i > 0:
    # Queremos multiplicar el valor factorial por el número
    # y todos los números por debajo de él hasta 1
    factorial *= i
    i -= 1

# Imprime el cálculo del factorial
print(f'El factorial de {num} es {factorial}')

