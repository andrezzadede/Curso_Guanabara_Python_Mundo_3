print('Bem vindo ao exercicio 90')

# Faça um programa que leia nome e media de um aluno, guardando também a situação em um dicionario(Se ele foi aprovado ou nao). No final, mostre o conteudo da estrutura na tela.

escola = dict()

escola['nome']= str(input('Nome do aluno: '))
escola['média']=float(input(f'Média de {escola["nome"]}: '))
if escola['média'] >= 7:
	escola['Situação']= 'Aprovado'
elif 5 <= escola['média'] < 7:
	escola['Situação'] = 'Recuperação'
else:
	escola['Situação']= 'reprovado'

for k, v in escola.items(): #conjunto chave e valor
	print(f'{k} é igual a {v}')
