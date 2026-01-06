# inicializando listas
linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()

# coletando números para a matriz e adicionando nas listas
for i in range(0, 3):
    l1 = int(input(f'Digite um valor para [0, {i}]: '))
    linha1.append(l1)
for i in range(0, 3):
    l2 = int(input(f'Digite um valor para [1, {i}]: '))
    linha2.append(l2)
for i in range(0, 3):
    l3 = int(input(f'Digite um valor para [2, {i}]: '))
    linha3.append(l3)
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)

# resposta
print(matriz)
print('-=' * 30)
print(f'[ {matriz[0][0]:^3} ][ {matriz[0][1]:^3} ][ {matriz[0][2]:^3} ]\n'
      f'[ {matriz[1][0]:^3} ][ {matriz[1][1]:^3} ][ {matriz[1][2]:^3} ]\n'
      f'[ {matriz[2][0]:^3} ][ {matriz[2][1]:^3} ][ {matriz[2][2]:^3} ]')
