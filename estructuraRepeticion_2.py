# Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o 
# iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, 
# respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.

# Número inicial de bacterias
colonia_a = 4
colonia_b = 10

# Tasas de crecimiento de las colonias
tasa_a = 0.03
tasa_b = 0.015

# Contador de días
días = 0

# La condición que termina el bucle es cuando
# la colonia A supera a la colonia B
while colonia_a <= colonia_b:
  # Usamos un operador de asignación con multiplicación
  colonia_a *= 1 + tasa_a
  colonia_b *= 1 + tasa_b
  # Contamos los días en cada iteración
  días += 1

# Resultado final
print(f'Necesitará {días} días para que la colonia A supere a la colonia B.')

