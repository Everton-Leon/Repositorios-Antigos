# importando bibliotecas
from random import randint
jogadas = 0
while True:

    # interface
    print('-=-' * 10)
    print('VAMOS JOGAR PAR OU IMPAR!')
    print('-=-' * 10)
    n = int(input('Digite um número: '))
    pc = randint(1, 10)

    # validação de dados
    jogador = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]
    while jogador not in 'PpIi':
        print('\033[1;31mOPÇÃO INVALIDA!\033[m')
        jogador = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]

    # respostas
    soma = n + pc
    if jogador in 'Ii' and soma % 2 == 1:
        print(f'Parabens! você jogou {n} e o computador {pc}. Total de {soma} IMPAR')
        jogadas += 1
    if jogador in 'Pp' and soma % 2 == 0:
        print(f'Parabens! você jogou {n} e o computador {pc}. Total de {soma} PAR')
        jogadas += 1
    if jogador in 'Pp' and soma % 2 == 1:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} IMPAR')
        break
    if jogador in 'Ii' and soma % 2 == 0:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} PAR')
        break
    print('====' * 15)
print(f'GAME OVER! Você venceu {jogadas} vezes.')
