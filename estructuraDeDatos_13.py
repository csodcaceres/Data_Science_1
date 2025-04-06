# Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario 
# debido a un excelente rendimiento del equipo. 
# El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras 
# de esta bonificación en los recursos. 
# Se te ha enviado una lista con los salarios que recibirán la bonificación: 
# [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 
# La bonificación de cada empleado no puede ser inferior a 200. 
# En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación 
# de cada salario en el valor correspondiente. 
# Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación 
# mínima y cuál fue el valor más alto de la bonificación proporcionada.


# Lista de salarios
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# Inicializamos las variables
diccionario_abonos = {}  # Diccionario de abonos
total_abono = 0  # Sumará todos los gastos en abonos
abonos_minimo = 0  # Almacenará la cantidad de abonos mínimos
mayor_abono = 0  # Almacenará el mayor valor de abono

# Recorremos toda la lista de salarios
for salario in salarios:
    # Calculamos el valor teórico del abono
    abono = salario * 0.1
    # Si el abono es inferior a 200,
    # ajustamos el valor del abono al mínimo (200)
    if abono < 200:
        abono = 200
    # Agregamos un nuevo dato en el diccionario con la clave abono
    diccionario_abonos[salario] = abono

# Recorremos todos los valores del diccionario de abonos
for abono in diccionario_abonos.values():
    # Contamos los salarios mínimos
    if abono == 200:
        abonos_minimo += 1
    # Verificamos si el abono leído es mayor que el valor almacenado en mayor_abono
    # Cada vez que el abono supere el valor de mayor_abono,
    # la variable mayor_abono será igual al abono, asignando un nuevo valor
    if abono > mayor_abono:
        mayor_abono = abono
    # Sumamos los abonos
    total_abono += abono
# Resultados
print(f'Abonos: {diccionario_abonos}')
print(f'Total de gastos en abonos: {total_abono}')
print(f'Número de empleados que recibieron el abono mínimo: {abonos_minimo}')
print(f'Mayor valor de abono: {mayor_abono}')

