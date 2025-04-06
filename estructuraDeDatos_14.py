# Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. 
# El equipo recopiló información sobre el número de especies de plantas y animales en cada área 
# del bosque y almacenó estos datos en un diccionario. 
# En él, la clave describe el área de los datos y los valores en las listas corresponden a las 
# especies de plantas y animales en esas áreas, respectivamente.

# {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 
# 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

# Escribe un código para calcular el promedio de especies por área e identificar el área con la 
# mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len()


# Especificamos los datos para un diccionario
datos = {'Área Norte': [2819, 7236],
         'Área Este': [1440, 9492],
         'Área Sur': [5969, 7496],
         'Área Oeste': [14446, 49688],
         'Área Centro': [22558, 45148]}
# Inicializamos las variables
suma_media = 0  # Sumará todos los promedios
mayor_diversidad = ''  # Almacenará el área con la mayor diversidad
mayor_suma = 0  # Almacenará la mayor suma de especies
# Recorremos las claves y elementos del diccionario
for área, especies in datos.items():
    # Sumamos el número de especies en cada área utilizando la función sum
    suma_especies = sum(especies)
    # Calculamos el promedio dividiendo la suma de las especies entre la cantidad de especies
    media = suma_especies / len(especies)
    # Imprimimos
    print(f'El {área} tiene un promedio de {media} especies')
    # Verificamos si la suma de especies es mayor que el valor almacenado de mayor_suma
    # Cada vez que suma_especies supere el valor de mayor_suma,
    # la variable mayor_suma será igual a suma_especies, asignando un nuevo valor
    # De manera similar, mayor_diversidad también se actualiza
    if suma_especies > mayor_suma:
        mayor_suma = suma_especies
        mayor_diversidad = área
    # Sumamos los promedios
    suma_media += media
# La media total será la suma_media dividida por la cantidad de áreas
media_total = suma_media / len(datos)
print(f'Media general de especies: {media_total}')
print(f'Área con la mayor diversidad biológica: {mayor_diversidad}')

