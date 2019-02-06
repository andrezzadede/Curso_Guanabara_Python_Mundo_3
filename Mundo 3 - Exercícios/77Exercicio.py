print('Bem vindo ao exercicio 77')

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos) depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais

lista = ('Aprender', 'Programar', 'Linguagem', 'Pyton', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for c in lista:
    print(f'\nNa palavra {c.upper()} temos: ', end= '')
    for letra in c:
        if letra.lower() in 'aeio':
            print(letra, end=' ')

