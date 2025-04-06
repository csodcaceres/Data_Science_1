# Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de 
# bacterias multiplicadas por día y se puede observar a continuación: 
# [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. 
# Con estos valores, crea un código que genere una lista que contenga el porcentaje de 
# crecimiento de bacterias por día, comparando el número de bacterias en cada día con el 
# número de bacterias del día anterior. 
# Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 
# 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

# Lista de crecimiento de bacterias
bacterias_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# Lista que almacenará las tasas de crecimiento
porcentaje_crecimiento = []
# Recorremos los índices de 1 a 9 para comparar los valores actuales con los anteriores
for i in range(1, len(bacterias_colonia)):
  # Realizamos el cálculo: 100 * (muestra_actual - muestra_anterior) / (muestra_anterior)
  porcentaje = 100 * (bacterias_colonia[i] - bacterias_colonia[i-1]) / (bacterias_colonia[i-1])
  # Agregamos el resultado a la lista porcentaje_crecimiento
  porcentaje_crecimiento.append(porcentaje)
# Resultado
print(f'Porcentajes de crecimiento:\n{porcentaje_crecimiento}')

