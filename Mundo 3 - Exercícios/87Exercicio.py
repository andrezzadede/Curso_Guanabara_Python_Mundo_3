#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados
#B) A soma dos valores da tecerceira coluna
#C) O maior dos valores da segunda linha

matriz = [[0,0,0], [0,0,0], [0,0,0]]

maior = scol = pares = 0

for l in range(0,3):
	for c in range(0,3):
		matriz[l][c] = int(input(f'Digite para [{l}][{c}] '))
		if matriz[l][c] % 2 == 0:
			pares += matriz[l][c]
			
print(f'Soma dos Pares: {pares}')
for l in range(0,3):
	scol += matriz[l][2]
print(f'A soma da terceira coluna é: {scol}')
#print(f'O maior numero da segunda linha: {seglinha}')

for c in range(0,3):
	if c ==0:
		maior = matriz[1][c]
	elif matriz[1][c] > maior:
		maior = matriz[1][c]
print(f'O maior número é:{maior}')

