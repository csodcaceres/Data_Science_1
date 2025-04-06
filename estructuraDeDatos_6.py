# Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida 
# para su análisis. Recopilamos el día, mes y año de una fecha y realizamos comprobaciones mes a mes,
#  confirmando si en febrero (sea o no un año bisiesto) el día coincide con lo que es posible. 
# También se analizan los meses que terminan en 31 o 30 días para evitar la existencia de fechas 
# inválidas en los datos.

# Recopilamos la fecha
dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
año = int(input('Ingrese el año: '))

# Análisis de febrero
if mes == 2:
  # Verificamos si es o no un año bisiesto
  if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
    dias_febrero = 29
  else:
    dias_febrero = 28
  # Verificamos si el día ingresado coincide con el máximo de días de febrero
  if dia >= 1 and dia <= dias_febrero:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Verificamos meses que terminan en 31 días
elif mes in [1, 3, 5, 7, 8, 10, 12]:
  if dia >= 1 and dia <= 31:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Verificamos meses que terminan en 30 días
elif mes in [4, 6, 9, 11]:
  if dia >= 1 and dia <= 30:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Si el mes no está entre 1 y 12
else:
  print('Fecha inválida')

