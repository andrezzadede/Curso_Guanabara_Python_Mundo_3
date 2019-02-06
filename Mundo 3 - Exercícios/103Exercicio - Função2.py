#Faça um programa que tenha uma função chamada ficha (), que tenha dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sifo informado corretamente

def ficha(nome='', gols=0):
	"""Nessa função é recebido o nome do jogador e a quantidade de gols que ele fez
	Existe um if para verificar se foi digitado o nome do jogador, caso não, ele é nomeado como desconhecido"""
	if nome == '':
		nome = 'desconhecido'
	print('=' * 40)
	print(f' O jogador {nome} marcou {gols} gols')
	print('=' * 40)

#Programa principal

ficha('', 40)
ficha('Mikey', 30)
ficha()

