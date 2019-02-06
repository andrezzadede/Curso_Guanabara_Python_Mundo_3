# Faça um programa que leia cinco valores númerios e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = list()
menor = 0
maior = 0
posiçaomenor = posiçaomaior = 0

for t in range (0, 5):
	if t == 0:
		valores.append(int(input('Informe um número: ')))
		menor = valores[t]
		maior = valores[t]
	else:
		valores.append(int(input('Fala outro número aí: ')))
		
		if menor > valores[t]:
			menor = valores[t]
		
		if maior < valores[t]:
			maior = valores[t]
print('='*20)
print(f'O maior número é {maior} nas posições: ', end='')
for i, v in enumerate(valores):
	if v == maior:
		print(f'{i}...', end='')
print()
print('=' * 20)

print(f'O menor número é {menor} e ele está nas posições:', end ='')
for i, v in enumerate(valores):
	if v == menor:
		print(f'{i}....', end='')

			

	

