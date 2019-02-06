# Crie um programa onde o usuario possa digitar vários valores numericos e cadastre-os em uma lista. Caso o numero já exista lá dentro, ele não será adicionado, no final, serão exibidos todos os valures unicos digitados em ordem crescente

numeros = list()

while True:
	n = int(input('Fale um número aí doidao: '))
	if n not in numeros:
		numeros.append(n)
		print('Valor adicionado com sucesso')
	else:
		print('Valor duplicado')
	c = ' '
	while c not in 'NS':
		c = str(input('Deseja continuar?[N/S]')).upper()
	if c == 'N':
		break
		
numeros.sort()
print(f'Você digitou {numeros}')
		
	
