# coletando dados do usuario
d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))

# calculando os dias vezes o preço
t = d*60

# calculando o total a ser pago
total = k*0.15+t

# reposta
print(f'O total a pagar é de R${total:.2f}')
