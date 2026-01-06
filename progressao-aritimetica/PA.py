# interface
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

# coletando dados do usuario
termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# calculando decimo termo
t = termo + (11 - 1) * r

# resposta
for c in range(termo, t, r):
    print(F'{c} --> ', end='')
print('Acabou')
