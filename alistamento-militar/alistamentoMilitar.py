# importando biblioteca
import datetime

# coletando dados do usuario
ano = int(input('Em que ano você nasceu? '))
sexo = int(input('''Qual seu sexo?
[ 1 ] - MASCULINO
[ 2 ] - FEMININO
opção: '''))

# realizando calculos
hoje = datetime.date.today().year
i = hoje - ano

# reposta
if i < 18 and sexo == 1:
    t = 18 - i
    print(f'Ainda vai se alistar. Faltam {t} anos.')
elif i > 18 and sexo == 1:
    t = i - 18
    print(f'Passou do tempo de alistamento. Deveria ter se alistado há {t} anos atrás.')
elif i == 18 and sexo == 1:
    print('Hora de se alistar!')
elif sexo == 2:
    print('Você não precisa se slistar!')
else:
    print('\033[1;31mOPÇÃO INVALIDA!')
