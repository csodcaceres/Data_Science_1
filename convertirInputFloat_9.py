# Podemos recopilar las tres notas con input y convertir la salida a números con decimales utilizando 
# la función float(). Luego, podemos mostrar el resultado del promedio entre las tres variables 
# sumando las notas con + y dividiendo la suma entre 3.

nota_1 = float(input('Ingrese la primer nota: '))
nota_2 = float(input('Ingrese la segunda nota: '))
nota_3 = float(input('Ingrese la tercer nota: '))

print(f'Media {(nota_1 + nota_2 + nota_3) / 3}')
