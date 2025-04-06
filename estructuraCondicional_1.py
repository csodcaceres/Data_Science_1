# Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el 
# número más grande

# Recolectamos los números
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
# Comparamos ambos números y determinamos cuál es el mayor
if num1 > num2:
    print(f'El primer número es mayor: {num1}')
elif num2 > num1:
    print(f'El segundo número es mayor: {num2}')
else: # En caso de que los números sean iguales
    print('Ambos números son iguales.')
    