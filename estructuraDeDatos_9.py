# Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. 
# Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide 
# con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.

# Inicializamos los datos
respuestas = []  # Lista para almacenar las respuestas
# Lista de respuestas correctas
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0  # Acumulará la nota total

# Recopilamos las respuestas del estudiante
for i in range(0, 10):
  respuestas.append(input(f'Introduzca la respuesta a la pregunta {i + 1}: ').upper())

# Verificamos si las respuestas coinciden y las sumamos a la nota
for i in range(0, 10):
  if respuestas[i] == gabarito[i]:
    nota += 1

# Mostrando la nota final
print(f'Nota final: {nota}')

