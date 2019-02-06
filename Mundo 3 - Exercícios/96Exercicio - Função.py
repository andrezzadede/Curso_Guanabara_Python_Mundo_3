# Faça um programa que tenha uma função chamada area que receba as dimensoes de um terreno retangular(largura e comprimento) e mostre a area do terreno

def area(largura, comprimento):
	terreno = largura * comprimento
	print(f'A area do terreno de {largura}X{comprimento} é de {terreno}')
	
	
larg = float(input('Qual a largura do terreno? '))
comp = float(input('Qual o comprimento do terreno? '))

area(larg, comp)

