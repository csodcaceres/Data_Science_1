# Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, 
# según la elección del usuario. Como ejemplo, para el número 2, 
# la tabla de multiplicar debe mostrarse en el siguiente formato:

# Tabla de multiplicar del 2: 2 x 1 = 2 2 x 2 = 4 [...] 2 x 10 = 20

# Solicita el número
num = int(input('Ingresa un número entero del 1 al 10: '))

# Generamos la tabla de multiplicar
print(f'Tabla de multiplicar del {num}:')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
