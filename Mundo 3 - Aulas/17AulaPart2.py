print('Bem vindo a aula 17 part 2')

pessoas = list()

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0]) # Pedro

print(pessoas[1][1]) # 19

print(pessoas[2][0]) # João

print(pessoas[1]) # Maria, 19

teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()

galera.append(teste) # Se deixar assim vai mudar as listas, acrescente (teste[:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

galeras = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galeras)

for pessoa in galeras:
	print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
	
lista = list()

dado = list()

for c in range(0, 3):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	lista.append(dado[:]) # Você coloca [:] para que ele nao mude nas duas listas ao editar
	dado.clear()
print(lista)
	# nesse for acima, ele faz pequenas listinhas usando o dado e vai acrescentando em uma lista grande chamada lista
	
for p in lista:
	if p[1] >=21:
		print(f'{p[0]} é maior de idade')
		
	else:
		print(f'{p[0]} é menor de idade')
