# Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, 
# necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que 
# recibirá calificaciones del 0 al 5 y verificará si son valores válidos. 
# Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario 
# ingrese un valor válido.

# Bucle para recopilar las 15 notas
for i in range(15):
  nota = float(input(f'Ingresa la nota del usuario {i}: '))

  # Verifica si la nota está entre 0 y 5
  # Si no lo está, el bucle se repetirá hasta que se obtenga un valor válido
  while (nota < 0) or (nota > 5):
    nota = float(input(f'Nota no válida, ingresa nuevamente la nota del usuario {i}: '))

print('Verificación completa. Todas las notas son válidas.')

