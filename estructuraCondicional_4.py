# Comparamos cada valor con los otros dos valores correspondientes a los otros dos años y 
# determinamos el valor más alto y el más bajo. Lo hacemos asignando inicialmente el valor de 
# precio_ano1 como el valor máximo y, si encontramos un valor mayor, actualizamos la variable mayor. 
# Utilizamos una lógica similar para encontrar el valor mínimo.

# Recolectamos los precios de los 3 años
precio_ano1 = float(input('Ingrese el precio promedio del automóvil en el primer año: '))
precio_ano2 = float(input('Ingrese el precio promedio del automóvil en el segundo año: '))
precio_ano3 = float(input('Ingrese el precio promedio del automóvil en el tercer año: '))
# Determinamos el valor más alto mediante comparaciones
mayor = precio_ano1
if precio_ano2 > mayor:
  mayor = precio_ano2
if precio_ano3 > mayor:
  mayor = precio_ano3
# Determinamos el valor más bajo mediante comparaciones
menor = precio_ano1
if precio_ano2 < menor:
  menor = precio_ano2
if precio_ano3 < menor:
  menor = precio_ano3
# Mostramos los resultados
print(f'El precio más alto fue de R$ {mayor}.')
print(f'El precio más bajo fue de R$ {menor}.')

