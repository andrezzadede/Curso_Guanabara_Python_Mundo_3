# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de zero, o dicionario receberá também o ano de contratação e o salario. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

carteira = dict()

carteira['nome'] = str(input('Qual seu nome'))
ano = int(input('Ano de nascimento'))
idade = date.today().year - ano
carteira['nascimento'] = idade
carteira['CTPS'] = int(input('Qual o numero da sua carteira de trabalho? [0 caso naao tenha]'))
if carteira['CTPS'] == 0:
	print(carteira)
else:
	carteira['contratacao']=int(input('Qual seu ano de contratação?'))
	carteira['salario']=float(input('Qual seu salario?'))
	carteira['aposentadoria'] = carteira['nascimento']+((carteira['contratacao']+35)-date.today().year)

for k, v in carteira.items():
	print(f'{k}, {v}')