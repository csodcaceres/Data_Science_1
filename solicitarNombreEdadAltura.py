# Podemos solicitar el nombre, la edad y la altura con la función input y asignar el resultado 
# de la salida a una variable. En el caso de la edad, es necesaria una conversión de la salida de 
# input a un valor entero con la función int(). Para la altura, es necesario realizar una conversión 
# al tipo de valor flotante con la función float(). A continuación, podemos imprimir el resultado de 
# las recopilaciones en la función print usando la formateación f-string.

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese se edad: ')
altura = input('Ingrese su ltura: ')

print(f'¡Hola {nombre}, tienes {edad} años y mides {altura} metros!')