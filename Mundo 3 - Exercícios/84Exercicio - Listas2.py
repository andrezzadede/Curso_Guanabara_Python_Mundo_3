# Faça um programa que leia nome e peso de várias pessoa, guardando tudo em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas
#B)Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

fit = list()
pesadas = list()
leves = list()
pesa = 0
le = 0
princ = list()

while True:
	fit.append(str(input('Qual seu nome gambazinho? ')))
	fit.append(float(input('E seu peso? ')))
	if len(princ) == 0:
		pesa = le = fit[1]
	else:
		if fit[1] > pesa:
			pesa = fit[1]
		if fit[1] < le:
			le = fit[1]
	princ.append(fit[:]) # Você cria duas listas e vai adicionando uma dentro da outra utilizando esse metodo
	fit.clear()
	resp = ' '
	while resp not in 'NS':
		resp = str(input('Deseja continuar? [N/S]')).upper()
	if resp == 'N':
		break
		


print('='*20)
print(f'Ao todo tiveram {len(princ)} pessoas cadastradas') # Aqui ele vai pegar a quantidade de registros cadastrados em princ
print(f'O menor peso foi {le} de ', end='')

for p in princ:
	if p[1] == le:
		print(f'{p[0]}...', end='')
print()
print(f'O maior é {pesa}', end='')
for q in princ:
	if q[1] == pesa:
		print(f'{q[0]}...', end='')




