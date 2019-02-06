print('Seja bem vindo a aula 17')

lista = ['Amora', 'Bane', 'Bruce', 'Iron']

lista.insert(4, 'Darth') #  Para adicionar um novo objeto

print(lista)

del lista [3] # Para remover um objeto

print(lista)

valores = list(range(4,11)) #Os valores podem ficar fora da ordem também, caso queira colocar em ordem é só colocar

valores.sort()

valores.sort(reverse=True) # Caso queira colocar os valores de trás para frente

print(len(valores)) # São quantos elementos tem em valores

print(valores)


print('\033[32mParte Prática\033[m')

listando = [2, 4, 1, 5]
listando[3] = 9
listando.append(7) #Adiciona um novo elemento
listando.sort()
listando.insert(2, 2) # Na posição 2 vai adicionar o 4 e passar os outros para frente
listando.pop() #Elimina o ultimo numero
listando.remove(2) # Só vai eliminar o primeiro elemento 2
print(listando)

print(f'Essa lista tem {len(listando)} elementos')

if 10 in listando:
    listando.remove(10)
else:
    print('Não achei o numero')

for c, v in enumerate(listando):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

print('Lendo valores')

valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

a = [3, 4, 5, 5]

b = a

b[2] = 10 # Assim, ele vai mudar o elemento tanto na lista a quanto na b

b = a[:] # Aqui você pode mudar depois em B e não vai mudar em A
