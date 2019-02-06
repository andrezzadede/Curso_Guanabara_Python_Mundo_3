print('Bem vindo ao exercicio 72')

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostra-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Fale um número aí entre 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente, ', end=' ')
print(f'Você digitou o número {contagem[num]}')

