#Crie um programa onde o usuario possa digitar sete valores númericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

principal = [[], []]

num = 0

for d in range(0, 7):
	num = int(input('Fala o numero jumes: '))
	if num % 2 == 0:
		principal[0].append(num)
	else:
		principal[1].append(num)
		
print('='*20)

print(f'Todos os números: {principal}')
print('='*20)
principal[0].sort()
print(f'Os valores pares: {principal[0]} ')
print('='*20)
principal[1].sort()
print(f'Os numeros impares: {principal[1]}')



