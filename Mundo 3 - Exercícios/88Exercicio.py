# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntas quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogsl = list()
jogos = int(input('Quantos jogos você quer gerar?'))
print('='*30)
tot = 1
while tot <= jogos:
	cont = 0
	while True:
		num = randint(1,60)
		if num not in lista:
			lista.append(num)
			cont +=1
		if cont >=6:
			break

	lista.sort()
	jogsl.append(lista[:])
	lista.clear()
	tot +=1
print('-=' * 3, f'Sorteando {jogos} jogos', '=' * 3)
for i, l in enumerate(jogsl):
	print(f'jogo {i}: {l}')


