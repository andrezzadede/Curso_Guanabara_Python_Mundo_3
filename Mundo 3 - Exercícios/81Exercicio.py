# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos numeros foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
total = 0

while True:
	lista.append(int(input('Fale um número: ')))
	total += 1
	c = ' '
	while c not in 'NS':
		c = str(input('Deseja continuar? [N/S]')).upper()
	if c == 'N':
		break
print(f'O total de números digitados foram {total}')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
	print('O valor 5 está na lista')
else:
	print('O valor 5 não está na lista')