# inicializando listas e variaveis
dados = list()
pessoas = list()
totp = 0
while True:

    # colentando dados e adicionando nas listas
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    totp += 1

    # fazendo verificações
    if totp == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    if resp == 'N':
        break

# repostas
print(f'No total {totp} foram cadastradas.')
print(f'O maior peso registrado foi {maior:.2f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso registrado foi {menor:.1f}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
