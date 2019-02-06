# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
#A) Quantas pessoas cadastradas. B)A média de idade. C) Uma lista com mulheres. D) Uma lista com idade acima da média

galera = list()
pessoa = dict()
soma = média = 0

while True:
	
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	
	while True:
		pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
		if pessoa['sexo'] in 'FM':
			break
		print('Erro! Por favor, digite apenas M ou F')
		
	pessoa['idade'] = int(input('Idade: '))
	soma += pessoa['idade']
	galera.append(pessoa.copy())
	
	while True:
		resposta = str(input('Quer continuar? [N/S]')).upper()[0]
		if resposta in 'SN':
			break
		print('Erro! Por favor, digite apenas S ou N')
		
	if resposta == 'N':
		break
# LENDO OS DADOS
print('-=' * 30)
#APRESENTANDO DADOS
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'A média da idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram', end='')
for p in galera:
	if p['sexo'] == 'F':
		print(f'{p["nome"]} ', end='')
print()
print('D) As pessoas acima da média são ', end='')
for p in galera:
	if p['idade'] > média:
		print(f'{p["nome"]} ', end='')
	print()
print('<<< Encerrado>>')

print (galera)
