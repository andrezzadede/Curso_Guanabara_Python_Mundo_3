#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = list()
pares = list()
impares = list()

while True:
	num.append(int(input('Fale um numero: ')))
	c = ' '
	while c not in 'SN':
		c = str(input('Deseja continuar?[N/S]')).upper()
	if c in 'N':
		break
for i, v in enumerate(num):
	if v % 2 == 0:
		pares.append(v)
	elif v % 2 == 1:
		impares.append(v)

		
print('='*30)

print(f'Lista inteira: {num}')

print('='*30)

print(f'Lista de números pares: {pares}')

print('='*30)

print(f'Lista de números impares: {impares}')

print('='*30)

print('FIM!')




