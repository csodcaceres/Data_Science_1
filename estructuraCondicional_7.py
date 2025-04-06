# Escribe un programa que pregunte en qué turno estudia la persona usuaria 
# ("mañana", "tarde" o "noche") y muestre el mensaje 
# "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.

# Recolectamos el turno de estudio
turno = input('Ingresa en qué turno estudias (mañana, tarde o noche): ')

# Comparamos la entrada con todas las opciones y mostramos el resultado.
if turno == 'mañana':
  print('¡Buenos Días!')
elif turno == 'tarde':
  print('¡Buenas Tardes!')
elif turno == 'noche':
  print('¡Buenas Noches!')
else:
  print('¡Valor Inválido!')

