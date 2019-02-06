print('Bem vindo ao exercicio 74')

#Crie um programa que vai gerar cinco números aleatórios e coloque em uma tupla. Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla
from random import randint

maior = menor = 0

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for i in range(0, 5):
	if i == 0:
		maior = n[i]
		menor = n[i]
	if maior < n[i]:
		maior = n[i]
	if menor > n[i]:
		menor = n[i]

print(n)
print(maior)
print(menor)

# OUUU

print(f'Maior{max(n)}')
print()
print(f'Menor{min(n)}')
