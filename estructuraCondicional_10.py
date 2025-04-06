# Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué 
# operación desea realizar. El resultado de la operación debe incluir información sobre el número, 
# si es par o impar, positivo o negativo, e entero o decimal.

# Recolectamos los números a operar y solicitamos la operación deseada por el usuario
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
operación = input('Ingrese la operación deseada (+, -, *, /): ')

# Verificamos la operación seleccionada y realizamos la operación matemática según la elección
if operación == '+':
    resultado = num1 + num2
elif operación == '-':
    resultado = num1 - num2
elif operación == '*':
    resultado = num1 * num2
elif operación == '/':
    resultado = num1 / num2
else: # Especificamos un resultado en caso de que el usuario no ingrese una de las operaciones correctamente.
    print('Operación no válida, el resultado de la operación será 0')
    resultado = 0

# Realizamos las mismas verificaciones que en preguntas anteriores para generar el informe del cálculo entre números
if resultado % 1 == 0:
    print('El resultado es un número entero.')
else:
    print('El resultado es un número decimal.')

if resultado > 0:
    print('El resultado es positivo.')
else:
    print('El resultado es negativo.')

if resultado % 2 == 0:
    print('El resultado es un número par.')
else:
    print('El resultado es un número impar.')

