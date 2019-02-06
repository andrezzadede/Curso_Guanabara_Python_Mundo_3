# Faça um programa que tenha uma função chamada contador, que receba tres parametros: inicio, fim e passo e realize a contagem;
#Seu programa tem que realizar tes contagens atraves da função criada: A) De 1 até 10, de 1 em 1. B) De 10 até 0, de 2 em 2. C) Uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
	print(f'Contagem de {inicio} até {fim} a cada {passo}')
	if passo < 0:
		passo *= - 1
	if passo == 0:
		passo = 1
	if inicio < fim:
		cont = inicio
		while cont <= fim:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont += passo
	else:
		cont = inicio
		while cont >= fim:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont -= passo
	print('Fim!')
	print('-' * 20)
	

print('*' * 30)

inicio = int(input('Informe o inicio'))
fim = int(input('Informe o fim'))
passo = int(input('Informe o passo'))
contador(inicio, fim, passo)
contador(1, 10, 1)
contador(10, 0, 2)