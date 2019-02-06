# Aprimore o desafio 93 para que ele funcione com varios jogadores. incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
todos = list()
jogador = dict()
gol = list()

while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome jogador: '))
	partidas = int(input(f'Quantas partidas {"nome"} jogou? '))
	gol.clear()
	for i in range(0,partidas):
		gol.append(int(input(f'Quantos gols ele fez na {i+1} partida? ')))
	jogador['gols'] = gol[:]
	jogador['total'] = sum(gol)
	todos.append(jogador.copy())
	while True:
		resp = str(input('Deseja continuar?[N/S]')).upper()[0]
		if resp in 'SN':
			break
		print('Erro! Sim ou não')
	if resp == 'N':
		break
print('=' * 30)
print('cod ', end='')
for i in jogador.keys():
	print(f'{i:<15}', end='')
print()
for k, v, in enumerate(todos):
	print(f'{k:>3} ', end='')
	for d in v.values():
		print(f'{str(d):<15}', end='')
	print()
print('*'*30)
while True:
	busca = int(input('Mostrar dados de quaal jogador? 999 PARA'))
	if busca ==999:
		break
	if busca >= len(todos):
		print(f'Erro! Nao existe esse jogador')
	else:
		print(f'----- Levantamento do jogador {todos[busca]["nome"]}')
		for i, g in enumerate(todos[busca]['gols']):
			print(f'    No jogo {i+1} fez {g} gols')
	print('-' * 40)
print('<< Volte sempre >>')

