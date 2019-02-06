# Crie um programa que tenha uma função chamada fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que será um valor logico (opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial
#exemplo print(fatorial(5, show=True) mostra o processo, se tiver false nao e faça um docstring

def fatorial(n=1, show=False):
	"""Docstring
	Calcula fatorial de um numero
	Essa função recebe dois parametros
	n: resonsavel pelo fatorial a ser calculado
	show: que decide se será mostrado o metodo de calculo ou não"""
	fatorial = 1
	for c in range(n, 0, -1):
		if show == True:
			print(c, end='')
			if c > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		fatorial *= c
	return fatorial


print('=' * 40)

print(fatorial(5, show=False))
print('=' * 40)

