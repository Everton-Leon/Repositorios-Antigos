# coletando dados do usuario
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

# calculando a area e quanto de tinta precisa para pintar
ar = l*a
t = ar/2

# resposta
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {ar}m^2.\nPara pintar essa parede, você precisará de {t}l de tinta!')
