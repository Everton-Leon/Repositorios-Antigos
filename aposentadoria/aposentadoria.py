# importando biblioteca
import datetime

# criando dicionario
dados = dict()
ano = datetime.date.today().year

# coletadndo dados
dados['nome'] = str(input('Nome: '))
anoN = int(input('Ano de nascimento: '))
dados['idade'] = ano - anoN                    # calculando idade
dados['ctps'] = int(input('Carteira de trabalho (0 não tem) : '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    aposent = (dados['contratação'] + 35) - anoN     # calculando aposentadoria

# mostrando dicionario
print('-=' * 30)
print(dados)
print('-=' * 30)

# resposta
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
print(f' - Aposentadoria tem o valor {aposent}')
