# Después de recolectar los 3 números, realizamos comparaciones siguiendo una lógica similar 
# a la pregunta anterior. Utilizamos el operador lógico and para determinar cuál es el número 
# más grande entre los 3 datos de productos, luego verificamos entre los dos más pequeños y f
# inalmente utilizamos print para mostrar los números en orden descendente mediante varias 
# declaraciones condicionales anidadas.

# Recolectamos los 3 números
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

# Comparación entre los 3 números
if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

