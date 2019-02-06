#Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteio() e somaPar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funçao vai mostrar a soma de todos os valores pares sorteaados

from random import randint
from time import sleep

def sorteio(lista):
	print('Sorteando valores: ', end='')
	for i in range (0, 5):
		n = randint(1, 10)
		lista.append(n)
		print(f'{n} ', end='', flush=True)
		sleep(0.3)
	print('Pronto!')


def somaPar(lista):
	soma = 0
	for valor in lista:
		if valor % 2 == 0:
			soma += valor
	print(f'Somando os valores pares da lista {lista}, temos {soma}')
	
	
numeros = list()
sorteio(numeros)
somaPar(numeros)
