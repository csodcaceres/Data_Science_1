# Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año.
# Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. 
# Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima 
# del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre 
# (Enero, Febrero, etc.).

# Recopilamos la lista de temperaturas mensuales
temperaturas_mensuales = []
for i in range(0, 12):
  temperaturas_mensuales.append(float(input(f'Ingrese la temperatura promedio del mes {i+1}: ')))
# Creamos una lista auxiliar para los nombres de los meses
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
# Calculamos el promedio
media_anual = sum(temperaturas_mensuales) / len(temperaturas_mensuales)

# Resultado
print('Temperaturas por encima del promedio en: ')
for i in range(0, 12):
  # Verificamos todas las temperaturas en comparación con la media anual
  if temperaturas_mensuales[i] > media_anual:
    # Dado que los índices de los meses corresponden a las temperaturas,
    # podemos imprimirlos con el mismo índice
    print(meses[i])


