# coletando dados do usuario
n = int(input('Digite um número: '))

# menu
op = int(input('''Em qual base númerica você quer que ele seja convertido?
[1] - Binário
[2] - Octal
[3] - Hexadecimal
opção: '''))

# reposta
if op == 1:
    b = format(n, "b")
    print(f'O número {n} convertido em Binário é {b}')
elif op == 2:
    b = format(n, "o")
    print(f'O número {n} convertido em Octal é {b}')
elif op == 3:
    b = format(n, "x")
    print(f'O número {n} convertido em Hexadecimal é {b}')
else:
    print(f'\033[1;31mOPÇÃO INVALIDA!')
