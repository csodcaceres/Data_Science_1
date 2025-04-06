# Recopilamos una frase utilizando la función input. Para asegurarnos de que los caracteres 
# no estén en mayúsculas, convertimos toda la frase a minúsculas utilizando el método lower y 
# luego aplicamos el método replace, definiendo el valor a reemplazar como 'e' y el nuevo valor 
# como 'f'. El resultado se muestra en un comando print.

frase = input('Ingrese una frase: ')

print(frase.lower().replace('e', 'f'))
