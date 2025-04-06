# El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de 
# los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos: 
# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 
# 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad 
# de cada sector, la edad media general entre todos los sectores y cuántas personas están por 
# encima de la edad media general.


# Especificamos los datos para un diccionario
datos = {'Sector A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Sector B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Sector C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Sector D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Inicializamos la variable que sumará todas las edades
total_edades = 0
# Recorremos las claves y elementos del diccionario
for sector, edades in datos.items():
  # Calculamos el promedio dividiendo la suma de las edades entre la cantidad de empleados en cada sector
  media_edad = sum(edades) / len(edades)
  # Imprimimos
  print(f'El {sector} tiene un promedio de {media_edad}')
  # Sumamos los promedios
  total_edades += sum(edades)
# La media total será el total_edades dividido por la cantidad de personas totales (sectores * empleados por sector)
media_total = total_edades / (len(edades) * len(datos))
print(f'La media de edad general es {media_total}')

# Inicializamos la variable que contará a todas las personas con edades por encima de la media
arriba_media = 0
# Recorremos nuevamente las claves y elementos del diccionario
for sector, edades in datos.items():
  # Leemos los elementos (edades) dentro de cada lista de edades en el diccionario
  for edad in edades:
    # Verificamos si el valor de la edad es superior a la media total
    if edad > media_total:
      # En caso de que el valor de la edad sea superior a la media, incrementamos en uno el contador
      arriba_media += 1
# Resultado
print(f'{arriba_media} personas están por encima de la edad media general')

