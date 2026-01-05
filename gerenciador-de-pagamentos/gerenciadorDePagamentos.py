# coletando dados do usuario
preço = float(input('Qual o preço do produto? R$'))

# menu
pagamento = int(input('''\033[1;36m*****ESCOLHA A CONDIÇÃO DO PAGAMENTO*****
[1] - A vista dinheiro/cheque
[2] - A vista no cartão
[3] - Até 2x no cartão
[4] - 3x ou mais no cartão
opção: '''))

# resposta
if pagamento == 1:
    desconto = preço - (preço * 10/100)
    print(f'PARABÉNS! Você ganhou 10% de desconto! de R${preço:.2f} foi para R${desconto:.2f}!')
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'PARABÉNS! Você ganhou 5% de desconto! de R${preço:.2f} foi para R${desconto:.2f}!')
elif pagamento == 3:
    print(f'Ficara o mesmo preço de R${preço:.2f}')
elif pagamento == 4:
    desconto = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${desconto / parcelas:.2F} com JUROS!')
    print(f'Será cobrado 20% de juros em cima do preço de R${preço:.2f}! o valor ficará R${desconto:.2f}!')
else:
    print('\033[1;31mOPÇÃO INVALIDA!')
