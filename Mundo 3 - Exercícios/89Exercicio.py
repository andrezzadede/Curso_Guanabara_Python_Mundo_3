#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

ficha = list()

while True:
	nome = str(input('Nome do aluno: '))
	n1 = float(input('1° Nota: '))
	n2 = float(input('2° Nota: '))
	média = (n1 + n2) / 2
	ficha.append([nome, [n1, n2], média])
	condição = ' '
	while condição not in 'NS':
		condição = str(input('Acabou? [N/S]')).upper()
	if condição in 'N':
		break
print('='*30)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
for i, a in enumerate(ficha):
	print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
	print('-' * 35)
	opc = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
	if opc == 999:
		print('Finalizando....')
		break
	if opc <= len(ficha) - 1:
		print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')