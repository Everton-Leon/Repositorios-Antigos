# colentando dados do usuario
t = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

# inicializando variaveis
t1 = 10
termos = t
cont = 1
total = 0
mais = 10

# lógica
while mais != 0:
    total += mais
    while cont <= total:
        print(termos, end=' ')  # resposta
        print(' --> ', end=' ')
        termos += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais (0 para parar)? '))
print(f'Progressão finalizada, com {total} termos mostrados') # fim do programa
