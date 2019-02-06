# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posição correta de inserção(sem usar o sort) no final, mostre a lista ordenada na tela.

lista = list()

for c in range (0, 5):
	n = int(input('Fala o valor:  '))
	if c ==0 or n > lista[-1]:
		lista.append(n) # Se for o primeiro só adiciona ou maior que o ultimo
	else:
		pos = 0
		while pos < len(lista):
			if n <= lista[pos]:
				lista.insert(pos,n)
				break
			pos +=1
print('='*30)
print(lista)
