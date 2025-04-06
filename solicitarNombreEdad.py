# 2 - Podemos solicitar el nombre y la edad con la función input y asignar el resultado de la 
# salida a una variable. En el caso de la edad, es necesaria una conversión de la salida de 
# input a un valor entero con la función int(). A continuación, podemos imprimir el 
# resultado de las recopilaciones en la función print usando la formateación f-string.

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')

print(f'¡Hola, {nombre}, tienes {edad} años!')