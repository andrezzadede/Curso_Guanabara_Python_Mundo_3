print('Bem vindo ao exercicio 75')

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares

valores= (int(input('Informe um número: ')),
         int(input('Fala outro aí: ')),
         int(input('Mais um: ')),
         int(input('O último agora:')))

print(f'Você digitou os valores {valores}')

print(f'O valor 9 apareceu: {valores.count(9)} vezes')
if 3 in valores:
    print(f'A posição do 3 é: {valores.index(3)+1}')
else:
    print('O valor 3 não existe na tupla')

for c in valores:
    if c % 2 == 0:
        print('Os valores pares são {} '.format(c, end=' '))


