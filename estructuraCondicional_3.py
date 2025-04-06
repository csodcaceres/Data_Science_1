# Escribe un programa que determine si una letra proporcionada por la persona usuaria es una 
# vocal o una consonante.

# Recolectamos la letra del usuario en minúsculas
letra = input('Ingrese una letra: ').lower()
vocales = 'aeiou' # cadena que contiene todas las vocales
# Verificamos si la letra está en las vocales con `in`
if letra in vocales:
    print('La letra es una vocal.')
else:
    print('La letra es una consonante.')
