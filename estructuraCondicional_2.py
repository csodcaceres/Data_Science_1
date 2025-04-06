# Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e 
# informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

# Recolectamos el porcentaje
variación = float(input('Ingrese el porcentaje de crecimiento: '))
# Verificamos si el valor es positivo o negativo con una comparación para ver si el número
# es mayor o menor que 0
if variación > 0:
    print(f'Hubo un crecimiento del {variación}%')
elif variación < 0:
    print(f'Hubo un decrecimiento del {variación}%')
else:
    print('No hubo crecimiento ni decrecimiento.')
