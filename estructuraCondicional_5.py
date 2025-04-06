#  Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el 
# producto más barato para comprar.

# Recolectamos el precio de tres productos
producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))

# Usamos el operador lógico `and` para determinar cuál es el precio más bajo entre los 3 productos
# ya que esto nos permite hacer una comparación de 3 entradas
if producto1 < producto2 and producto1 < producto3:
    print('El primer producto es el más barato.')
elif producto2 < producto1 and producto2 < producto3:
    print('El segundo producto es el más barato.')
else:
    print('El tercer producto es el más barato.')

