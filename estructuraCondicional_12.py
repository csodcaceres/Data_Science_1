# Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, 
# si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. 
# En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 
# 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. 
# El precio por litro de diésel es de R 2,00 y el precio de etanol es de R 1,70
# 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible 
# (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. 
# Ten en cuenta algunas sugerencias:

# El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor 
# del descuento.

# El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro 
# por la cantidad de litros menos el valor del descuento resultante del cálculo.



# # Recolectamos la cantidad de litros y el tipo de combustible,
# convirtiendo el carácter en mayúsculas para facilitar nuestro análisis
cantidad_litros = float(input('Ingrese la cantidad de litros vendidos: '))
tipo_combustible = input('Ingrese el tipo de combustible (E para etanol y D para diésel): ').upper()

# Verificamos primero el tipo de combustible
if tipo_combustible == 'E':
  # Establecemos el precio por litro de etanol
  precio_litro = 1.70
  # Según la cantidad de litros, establecemos el descuento correspondiente
  if cantidad_litros <= 15:
    descuento = 0.02
  else:
    descuento = 0.04
elif tipo_combustible == 'D':
  # Establecemos el precio por litro de diésel
  precio_litro = 2.00
  # Según la cantidad de litros, establecemos el descuento correspondiente
  if cantidad_litros <= 15:
    descuento = 0.03
  else:
    descuento = 0.05
# En caso de error en la especificación del tipo de combustible,
# consideramos las entradas como no válidas y establecemos los precios y descuentos en 0
else:
    print('Entradas no válidas!')
    precio_litro = 0
    descuento = 0

# Calculamos el valor del descuento, seguido del cálculo del precio descontado
valor_descuento = precio_litro * cantidad_litros * descuento
valor_pagado = precio_litro * cantidad_litros - valor_descuento

# Resultado
print(f'Valor a pagar por el cliente: R$ {valor_pagado}')

