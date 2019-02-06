# Faça um programa que tenha a função chamada escreva(), que vai receber um texto qualquer como paramentro e mostre uma mensagem com tamanho adaptavel.

def escreva(escrita):
	t = len(escrita) + 4
	print('-' * t )
	print(f'  {escrita}')
	print('-' * t)


texto = str(input('Informe o texto, linda: '))

escreva(texto)