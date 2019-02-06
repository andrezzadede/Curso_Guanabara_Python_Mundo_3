#Crie um programa que crie uma matriz de dimensão 3X3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

b = list()


for l in range(0, 3):
	for c in range(0,3):
		a[l][c] = (int(input(f'Fala o número para [{l}], [{c}]: ')))

print('='*30)

for l in range(0,3):
	for c in range(0, 3):
		print(f'[{a[l][c]:^5}]', end='')
	print()