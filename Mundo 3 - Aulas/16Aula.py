print ('='*20, 'Bem vindo a aula 16', '=' *20)

print('Variáveis compostas - Tuplas')

print('='*20)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Tuplas são imutáveis, ou seja, não posso atribuir valores novos as tuplas

print(lanche[3])

print(lanche[-2])

print(lanche[1:3])

print(lanche[:2])

print(lanche[2:])

print(lanche[-2:])

print(sorted(lanche))

print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para um caralho!')

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição: {cont}' )

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posiçao {pos}')

a = (2, 4, 5)

b = (5, 8, 1, 2)

c = a + b

print(c)

print(c.count(5)) # Quantas vezes aparece o cinco em C?

print(c.index(8)) # Mostra a posição do número

pessoa = ('Andrezza', 21, 'F', 50.00)

print(pessoa)