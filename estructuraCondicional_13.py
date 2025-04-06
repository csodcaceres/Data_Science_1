# En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas 
# anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos 
# de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. 
# A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

# Para una variación superior al 20%: bonificación para el equipo de ventas.

# Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.

# Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.

# Para bonificaciones inferiores al -10%: recorte de gastos.

# Si necesitas ayuda, las opciones de solución para las actividades estarán disponibles en la sección "Opinión del instructor".

# Recolectamos las ventas de los dos años
venta_2022 = float(input('Ingrese la cantidad de ventas en 2022: '))
venta_2023 = float(input('Ingrese la cantidad de ventas en 2023: '))

# Calculamos la variación porcentual entre las ventas de los años 2022 y 2023
var_porcentual = 100 * (venta_2023 - venta_2022) / (venta_2022)

# Análisis condicional de la variación porcentual para determinar la sugerencia a enviar
if var_porcentual > 20:
    print('Bonificación para el equipo de ventas.')
elif 2 <= var_porcentual <= 20:
    print('Pequeña bonificación para el equipo de ventas.')
elif -10 <= var_porcentual < 2:
    print('Planificación de políticas de incentivo a las ventas.')
else:
    print('Recorte de gastos.')

