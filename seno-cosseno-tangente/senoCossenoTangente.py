# importando biblioteca
import math

# coletando dados do usuario
a = float(input('Digite o ângulo: '))

# convertendo o valor em rediando
xr = math.radians(a)

# reposta
print(f'O seno de {a} é {math.sin(xr):.2f}\nO cosseno de {a} é {math.cos(xr):.2f}\nA tangente de {a} é {math.tan(xr):.2f}')
