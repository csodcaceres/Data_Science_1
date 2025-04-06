# Recopilamos una frase utilizando la función input. Para asegurarnos de que los caracteres no 
# estén en mayúsculas, convertimos toda la frase a minúsculas utilizando el método lower y 
# luego aplicamos el método replace, definiendo el valor a reemplazar como 'a' y el nuevo valor 
# como el carácter 64 según la tabla Unicode, que corresponde al carácter @. El resultado se 
# muestra en un comando print.

frase = input('Escribe una frase: ')
print(frase.lower().replace('a',chr(64)))
