# importando arquivos
from func import *
from arquivo import *

# inicializando arquivo
arq = 'cursoemvideo.txt'

# verificando se ele existe e criando arquivo
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:

    # criando o menu de opções e fazendo os comandos funcionarem
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Encerrando programa... Volte sempre')
        break
    else:
        print('\033[1;31mErro! Digite uma opção valida\033[m')

