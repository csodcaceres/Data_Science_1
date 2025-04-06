# En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. 
# Escribe un programa que calcule al ganador de la elección. 
# La votación se realizó de la siguiente manera:

# Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

# También se contaron los votos nulos (representados por el número 5) 
# y los votos en blanco (representados por el número 6).

# Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, 
# los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

# Inicializamos las variables contadoras
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_blanco = 0

# Inicio del bucle para leer los votos
for i in range(0, 20):
    voto = int(input('Ingresa tu voto: '))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_blanco += 1
    else:
        print("Voto inválido.")

print(f'Votos candidato 1: {votos_candidato1}')
print(f'Votos candidato 2: {votos_candidato2}')
print(f'Votos candidato 3: {votos_candidato3}')
print(f'Votos candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos en blanco: {votos_blanco}')
print(f'Porcentaje de votos nulos: {(votos_nulos / 20 * 100)}')
print(f'Porcentaje de votos en blanco: {(votos_blanco / 20 * 100)}')

