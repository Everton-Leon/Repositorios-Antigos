# dados do cardapio
listagem = ('Hamburguer', 16.50, 'Pastel', 5.00, 'Suco', 6.99, 'Refrigerante', 7.50)

# interface
print('_' * 30)
print(f'LISTAGEM DE PREÇOS'.center(30))
print('_' * 30)

# resposta
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>5}')
