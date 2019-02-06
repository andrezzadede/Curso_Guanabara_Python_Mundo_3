print('Bem vindo a aula 19 - Dicionarios')

# Declarando um dicionario

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

# Adicionando um novo elemento

dados['sexo'] = 'M'

# remover elemento

del dados['idade']

print(dados)

filme = {'titulo':'Star Wars', 'ano':1977, 'diretor': 'George'}
# Para exibir só os elementos dentro dos indices
print(filme.values())
#Se quiser exibir só os indices
print(filme.keys())
#Se quiser exibir tudo
print(filme.items())

for k, v in filme.items():
	print(f'{k}, {v}')
	
locadora = list()

#print(locadora[0]['ano']) # Aqui vai pegar o elemento 0 da lista e mostrar o ano do elemento

pessoas = {'nome': 'Andrezza', 'sexo': 'F', 'idade':22}
print(pessoas['nome'])
print(f'A {pessoas["nome"]}') # precisa de aspas duplas

for k in pessoas.keys():
	print(k) # Se eu quiser mostrar apenas os indices
	
for k in pessoas.items():
	print(k) # Mostra tudo

pessoas['nome'] = 'Dede' # Para mudar o elemento

print(pessoas['nome'])

# Criando um dicionario dentro de lista
brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado)
brasil.append(estado2)
print(brasil)

print(brasil[0]['uf'])

est = dict()
br = list()

for c in range(0,3):
	est['uf']= str(input('unidade federativa'))
	est['sigla']=str(input('Sigla'))
	br.append(est.copy()) # Para copiar o conteudo do dicionario para a lista
print(br)

for e in br:
	for k, v, in e.items():
		print(f'O campo {k} tem o valor {v}')