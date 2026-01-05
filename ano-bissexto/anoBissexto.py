# importando biblioteca
from datetime import date

# perguntando ano ao usuario
a = int(input('Qual ano você quer analizar? Coloque 0 para analizar o ano atual: '))

# reposta
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'{a} é um ano bissexto!')
else:
    print(f'{a} Não é um ano bissexto!')
