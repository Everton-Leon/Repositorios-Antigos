# interface
print('-=-' * 20)
print('Analizador de Triângulos')
print('-=-' * 20)

# coletando dados do usuario
r1 = float(input('Comprimento 1: '))
r2 = float(input('Comprimento 2: '))
r3 = float(input('Comprimento 3: '))

# resposta
if r3 < r1+r2 and r1 < r2+r3 and r2 < r3+r1:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')
