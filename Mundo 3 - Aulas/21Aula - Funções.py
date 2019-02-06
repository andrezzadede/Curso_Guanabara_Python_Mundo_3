# Interactive HELP

#help(print)

# Ele mostra o que cada função já do Python faz.

#print(input.__doc__)

# Dogstring

def contador(i,f,p):
	"""Faz uma contagem e mostra na tela
	:param i: inicio da contagem
	:param f: fim da contagem
	:param p: passo da contagem
	:return: sem retorno
	: isso é uma dogstring onde eu documento minhas funções"""

	c = i
	while c <= f:
		print(f'{c}', end='..')
		c += p
	print('FIM')

contador(2, 10, 2)

help(contador)

#Parametros opcionais
#Posso atribuir zero a todos os parametros e aí caso eu não digite um ou outro parametro, vai funcionar a função do mesmo jeito
def somar(a, b, c=0):
	s = a + b + c
	print(f'A soma vale {s}')
	
	
somar(3, 2, 5)
somar(8, 4)

#Escopo de variaveis

def teste():
	x = 8 # Variavel local
	print(f'Na função teste, n vale{n}')
	print(f'Na função teste, x vale{x}')

n = 2 # Variavel global
print(n)
print(f'No programa pricipal, n vale{n}')



def funcao():
	n = 4
	print(f'N dentro vale{n}')
	
	
n = 5
funcao()
print(f'N fora vale{n}')

def t(b):
	global v
	a = 8
	b +=4
	c=2
	print(f'A dentro vale {a}')
	print(f'B dentro vale{b}')
	print(f'C dentro vale{c}')
	
	
a = 5
t(a)
print('-' * 40)
# Return
def soma(a=0, b=0, c=0):
	s = a + b + c
	return s


resp = soma(2, 4, 5)

print(f'A soma deles vale {resp}')

def fatorial(num=1):
	f = 1
	for c in range(num, 0, -1):
		f *= c
	return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual {fatorial(n)}')

def par(d=0):
	if d % 2 ==0:
		return True
	else:
		return False
	
	
v = int(input('Digite um numero'))
if par(v):
	print('É par!')
else:
	print('NAO É PAr')