#Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep

def maior(* Y):
	maior = 0
	i = 0
	lista =list()
	while i < len(Y):
		lista.append(Y[i])
		if maior < lista[i]:
			maior = lista[i]
		i += 1
	print(f'Analisando os números: {lista}')
	print(f'O maior número é: {maior}')
	print('~' * 30)
	sleep(1)



maior(3, 2, 6, 7, 9, 1)
maior(4, 33, 21, 5, 42, 59, 32, 69)
maior(3, 4, 0, 29, 1000, 2942, 943)
maior()