# Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por 
# encima de 3000 reales y calcula el porcentaje con respecto al total de compras.

# Datos de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Variable que contará cuántas compras se realizaron por encima de 3000
contador_acima_3000 = 0

# Totl de compras
cantidad_compras = len(gastos)

# Usamos un bucle para recorrer la lista de gastos
for gasto in gastos:
  # Verificamos si el elemento está por encima de 3000
  if gasto > 3000:
    # Sumamos uno al contador si hay algún valor por encima de 3000
    contador_acima_3000 += 1

# Con el conteo podemos calcular el porcentaje de valores por encima de 3000 entre todas las compras
porcentaje_acima_3000 = 100 * contador_acima_3000 / cantidad_compras

# Resultado
print(f'{contador_acima_3000} compras estuvieron por encima de R$3000,00.')
print(f'{porcentaje_acima_3000}% de los gastos estuvieron por encima de R$3000,00.')

