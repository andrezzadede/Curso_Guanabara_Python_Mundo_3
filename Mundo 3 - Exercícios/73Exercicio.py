print('Bem vindo ao exercicio 72')

# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebool, na ordem de colocação, depois mostre: A) apenas os 5 primeiros colocados b) os últimos 4 colocados da tabela c) uma lista com os times e ordem alfabetica d) em que posição está o time da chapecoense

times = ('São Paulo', 'Chapecoense', 'Santos', 'Palmeiras', 'Vasco', 'Flamengo', 'Fluminense', 'Gremio', 'Bahia', 'Internacional', 'Atlético', 'Cruzeiro', 'Botáfogo', 'Sport', 'Vitória', 'Atlético-PR', 'Ceará', 'Paraná', 'América', 'Ceará')

print(f'Os primeiros cinco colocados são: {times[:5]}')
print('='*20)
print(f'Os quatro últimos colocados são: {times[16:]}')
print('='*20)
print(f'Em ordem alfabetica: {sorted(times)}')
print('='*20)
print(f'Chapecoense está na posição: {times.index("Chapecoense")+1}')