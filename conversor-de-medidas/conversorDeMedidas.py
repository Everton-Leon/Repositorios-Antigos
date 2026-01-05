# coletando dados do usuario
n = float(input('Digite o valor: '))

# convertendo o valor
d = 10*n
c = 100*n
m = 1000*n
da = n/10
h = n/100
k = n/1000

# resposta
print(f'{n}m correspode a\n{k}km\n{h}hm\n{da}dam\n{d:.0f}dm\n{c:.0f}cm\n{m:.0f}mm')
