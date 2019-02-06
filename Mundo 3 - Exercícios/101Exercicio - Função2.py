#Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal(frase) indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleições

# Com 65 é opcional


def voto(ano):
	from datetime import date
	idade = date.today().year - ano
	if idade < 16:
		return f'Com {idade} anos o voto é: Não vota'
	elif 16 <= idade < 18 or idade > 65:
		return f' Com {idade} anos o voto é: Opcional'
	else:
		return f'Com {idade} anos o voto é: OBRIGATORIO'
	


print('~' * 40)
nascimento = int(input('Qual seu ano de nascimento?'))
print(voto(nascimento))
print('~' * 40)
	

