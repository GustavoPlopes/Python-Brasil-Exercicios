# endo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas: Para homens: (72.7*h) - 58, Para mulheres: (62.1*h) - 44.7
from modulos_úteis import menu

menu('PESO IDEAL \033[1;34mHOMEM\033[m & \033[1;35mMULHER\033[m')
while True:
    sexo = str(input('Qual seu sexo? [\033[1;34mM\033[m/\033[1;35mF\033[m]? ')).strip().upper()
    if sexo not in 'MF':
        print('\033[1;31m!ERRO! Digite apenas "M" para masculino ou "F" para feminino\033[m')
    elif sexo in 'MF':
        break

altura = float(input('Digite a sua altura: '))

if sexo == 'M':
    homem = (72.7 * altura) - 58
    print(f'{"-"*30}')
    print(f'Seu peso ideal é {homem:.2f}Kg')
elif sexo == 'F':
    mulher = (62.1 * altura) - 44.7
    print(f'{"-" * 30}')
    print(f'Seu peso ideal é {mulher:.2f}Kg')
