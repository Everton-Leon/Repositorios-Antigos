# importando bibliotecas
import random
import time

# sorteando número do computador
a = random.randint(0,5)

# interface
print('\033[1;36m-=-' * 20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADVINHAR...')
print('\033[1;36m-=-\033[m' * 20)

# resposta do usuario
n = int(input('Em qual número eu pensei? '))

# revelando o ganhador
print('''Processando...''')
time.sleep(3)
if n == a:
    print('PAREBENS! você conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no número {a} e não no {n}!')
