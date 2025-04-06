# Recopilamos una frase utilizando la función input. Para asegurarnos de que los caracteres no 
# estén en mayúsculas, convertimos toda la frase a minúsculas utilizando el método lower y 
# luego aplicamos el método replace, definiendo el valor a reemplazar como 's' y el nuevo valor 
# como el carácter 36 según la tabla Unicode, que corresponde al símbolo $. El resultado se 
# muestra en un comando print.

frase = input('Escribe una frase: ')
print(frase.lower().replace('s',chr(36)))
