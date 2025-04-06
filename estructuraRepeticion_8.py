# Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. 
# Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la 
# distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. 
# La entrada de datos se detendrá al ingresar un número negativo.

# Recopilamos las edades de los clientes
edad = int(input('Ingresa la edad (o un número negativo para finalizar): '))

# Inicializamos las variables de conteo
contador_0_25 = 0 # contador de edades entre 0 y 25
contador_26_50 = 0 # contador de edades entre 26 y 50
contador_51_75 = 0 # contador de edades entre 51 y 75
contador_76_100 = 0 # contador de edades entre 76 y 100

# Nuestro código se ejecuta hasta que el valor de edad sea negativo
while edad >= 0:
    # Contamos cada caso
    if edad >= 0 and edad <= 25:
        contador_0_25 += 1
    elif edad >= 26 and edad <= 50:
        contador_26_50 += 1
    elif edad >= 51 and edad <= 75:
        contador_51_75 += 1
    elif edad >= 76 and edad <= 100:
        contador_76_100 += 1

    # Repetimos el proceso de entrada de datos hasta que se ingrese un número negativo
    edad = int(input('Ingresa la edad (o un número negativo para finalizar): '))

# Mostramos los resultados
print('Distribución de edades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)
