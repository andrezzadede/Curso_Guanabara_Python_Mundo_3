# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogdor e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gol = list()

jogador['nome'] = str(input('Nome jogador: '))
partidas = int(input(f'Quantas partidas {"nome"} jogou? '))
for i in range(0,partidas):
	gol.append(int(input(f'Quantos gols ele fez na {i+1} partida? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
print('=' *30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
	print(f'Na partida {i} fez {v} gols')
print(f'Foi o total de {jogador["total"]}')


