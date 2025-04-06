# Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. 
# Los datos de ventas se han almacenado en un diccionario:

# {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 
# 'Producto F': 30}

# Escribe un código que calcule el total de ventas y el producto más vendido.


# Diccionario de ventas
datos_ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

# Inicializamos las variables
total_ventas = 0  # Sumará todas las ventas
producto_mas_vendido = ''  # Almacenará el nombre del producto más vendido
unidades_producto_mas_vendido = 0  # Almacenará la cantidad más alta de ventas

# Recorremos las claves y elementos del diccionario
for producto in datos_ventas.keys():
    # Sumamos el total de ventas
    total_ventas += datos_ventas[producto]
    # Verificamos si el valor de ventas actual (datos_ventas[producto]) es mayor que el valor almacenado en unidades_producto_mas_vendido
    # Cada vez que datos_ventas[producto] supere el valor en unidades_producto_mas_vendido,
    # la variable unidades_producto_mas_vendido será igual a datos_ventas[producto], asignando un nuevo valor
    # De manera similar, producto_mas_vendido también se actualiza con el producto actual
    if datos_ventas[producto] > unidades_producto_mas_vendido:
        unidades_producto_mas_vendido = datos_ventas[producto]
        producto_mas_vendido = producto
# Resultados
print(f'Total de ventas es {total_ventas}')
print(f'{producto_mas_vendido} es el más vendido')

