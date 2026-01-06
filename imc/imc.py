# interface
print('\033[1;36m-=-\033[m' * 10)
print(f'\033[1;36m{"CALCULE SEU IMC".center(30)}')
print('\033[1;36m-=-\033[m' * 10)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# calculo do imc
imc = peso / altura**2

# resposta
if imc < 18.5:
    print(f'IMC = {imc:.1f}. Você está ABAIXO DO PESO!.')
elif imc >= 18.5 and imc < 25:
    print(f'IMC = {imc:.1f}. \033[1;33mPARABÉNS!\033[m Você está com o \033[1;33mPESO IDEAL!')
elif imc >= 25 and imc < 30:
    print(f'IMC = {imc:.1f}. \033[1;35mCUIDADO!\033[m Você está com \033[1;35mSOBREPESO!')
elif imc >= 30 and imc < 40:
    print(f'IMC = {imc:.1f}. \033[1;31mALERTA!\033[m Você está com \033[1;31mOBESIDADE!')
else:
    print(f'IMC = {imc:.1f}. \033[1;31mCOM O PÉ NA COVA JÁ! OBESIDADE MORBIDA!')
