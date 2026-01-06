# colentando dados
ex = str(input('Digite a expressão: '))

# verificando se é uma expressão
a = ex.count('(')
b = ex.count(')')

# resposta
if a == b:
    print('A expressão é valida')
else:
    print('A expressão é invalida')
