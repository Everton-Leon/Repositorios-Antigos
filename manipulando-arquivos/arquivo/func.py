# criando Funções
def menu(lista):
    titulo('MENU PRINCIPAL')
    cont = 1
    for i in lista:
        print(f'\033[1;33m{cont} -\033[m \033[1;34m{i}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[1;32mOpção: \033[m')
    return opc


def linha(num = 40):
    return '-' * num


def titulo(msg):
    print(linha())
    print(msg.center(40))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            print('O usuario prefeiru não informar o valor.')
            return 0
        except:
            print(f'\033[1;31mErro! Por favor digite um número inteiro válido!\033[m ')
            continue
        else:
            return int(a)


def pessoa(nome, idade):
    print(f'{nome:<25}      {idade:>3}')









