#Crie um programa onde o usuario digite uma expressao qualquer que use paratenses. Seu aplicativo deverá analisar se a expressao passada está com os paratenses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressao: '))

pilha = []

for simb in expressao:
	if simb == '(':
		pilha.append('(')
	elif simb == ')':
		if len(pilha)>0:
			pilha.pop() # remove o ultimo elemento da lista
		else:
			pilha.append(')')
			break
			
if len(pilha) == 0:
	print('Sua expressao é valida')
else:
	print('Errado')
	