# Después de recolectar los valores de los 3 lados de un triángulo, debemos verificar si 
# realmente pueden formar un triángulo siguiendo el consejo "Tres lados forman un triángulo 
# cuando la suma de cualquier par de lados es mayor que el tercer lado". 
# Esta verificación se puede realizar con el operador "and". Luego, podemos verificar si todos los 
# lados son iguales, lo que forma un triángulo equilátero, o si todos los lados son diferentes, 
# lo que forma un triángulo escaleno. Estas verificaciones se pueden realizar con el operador 
# "and" y los operadores "== y "! =". Finalmente, utilizamos "else" para el caso de un triángulo 
# isósceles.

# Recolectamos los lados de un triángulo
print('Estamos recopilando los lados de un triángulo.')
lado1 = float(input('Ingresa la longitud del primer lado: '))
lado2 = float(input('Ingresa la longitud del segundo lado: '))
lado3 = float(input('Ingresa la longitud del tercer lado: '))

# Verificamos si los lados pueden formar un triángulo
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('¡Los valores pueden formar un triángulo!')
    # Comparamos los lados para determinar el tipo de triángulo
    if (lado1 == lado2) and (lado2 == lado3):
        print('El triángulo es equilátero.')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('El triángulo es escaleno.')
    else:
        print('El triángulo es isósceles.')
else:
    print('¡Los valores no pueden formar un triángulo!')

