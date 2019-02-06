def lin():
	print('-' * 30)
	

#Programa principal

lin()
print(' Curso em Video')
lin()
print(' Aprenda Python')
lin()
print(' Gustavo Guanabara')
lin()

print('Segunda opção')

def mensagem(msg):
	print('-' * 30)
	print(msg)
	print('-' * 30)
	
mensagem('Sistema de alunos')
nome = 'Andrezza'
mensagem(nome)

print('*' * 50)

def soma(a, b):
	s = a + b
	print(s)
	
#Programa principal
soma(3, 3)
soma(2, 4)

lin()

def somando(a, b):
	print(f'A = {a} e B = {b}')
	s = a + b
	print(f'A soma A + B = {s}')
	
somando(3, 6)

lin()

print('Empacotando')
# Basicamente ele pega todos os parametros e desempacota
def contador(* num):
	for valor in num:
		print(f'{valor} ', end='')
	print('FIM!')
	
	tam = len(num)
	print(f'O total de numeros são {tam}')
	
	s = 0
	for valores in num:
		s += valores
	print(f'Somando os valores {num} temos {s}')
	
	
contador(2, 4, 4)
contador(2, 5, 3, 6, 6)


lin()

def dobra(lst):
	pos = 0
	while pos < len(lst):
		lst[pos] *=2
		pos += 1
	
	
valores = [3, 5, 3, 2]
dobra(valores)
print(valores)
