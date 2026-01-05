# importando biblioteca
import math

# coletando dados do usuario
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto ajacente: '))

# calculando a hipotenusa
h1 = math.hypot(co, ca)

# resposta
print(f'A hipotenusa dos catetos {co} e {ca} é {h1:.2f}')
