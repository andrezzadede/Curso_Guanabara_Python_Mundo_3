print('bem vindo ao exercicio 76')

#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia. No final, mostre uma listagem de preços, organizando os dados em forma tabular, ou seja, uma lista.

compras = ('Morago', 4.33, 'Maçã', 3.32, 'Banana', 4.44, 'Uva', 5.0)

for cont in range (0, len(compras)):
    if cont % 2 ==0:
        print(f'{compras[cont]:.<30}', end=' ')
    else:
        print(f'R${compras[cont]:>5.2f}')






