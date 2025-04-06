# Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel 
# [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
# Con estos valores, crea un programa que calcule el promedio de gastos. 
# Sugerencia: usa las funciones integradas sum() y len().

# Datos de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Calculamos el promedio encontrando el valor total de gastos con la función sum
# y la cantidad total de compras realizadas con len
total_gastos = sum(gastos)
cantidad_compras = len(gastos)
media_gastos = total_gastos / cantidad_compras
# Resultado
print(f'El promedio de gastos es {media_gastos} reales.')

