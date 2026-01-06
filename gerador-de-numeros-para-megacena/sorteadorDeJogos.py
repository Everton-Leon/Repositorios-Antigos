# importando bibliotecas
from random import randint
from time import sleep

# criando listas
palpites = list()
resultado = list()
tot = 1

# interface
print('-=' * 20)
print(f'{"JOGA NA MEGA CENA".center(40)}')
print('-=' * 20)

# coletando dados do usuario
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(F'-==== SORETEANDO {jogos} JOGOS ====-')
while tot <= jogos:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    resultado.append(palpites[:])
    palpites.clear()
    tot += 1

# respota
for c, i in enumerate(resultado):
    sleep(1)
    print(f'Jogo {c+1}: {i}')
print('==== <BOA SORTE> ====')
