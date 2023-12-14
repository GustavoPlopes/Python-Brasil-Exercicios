# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numero_inteiro_1 = int(input('Digite o \033[0;31mprimeiro\033[m numero inteiro: '))
numero_inteiro_2 = int(input('Agora o \033[0;31msegundo\033[m inteiro: '))
numero_real = float(input('Digite por \033[0;31multimo\033[m um numero real: '))

calculo_1 = (2 * numero_inteiro_1) + (numero_inteiro_2 / 2)
calculo_2 = (numero_inteiro_1 + numero_real) * 3
calculo_3 = numero_real * numero_real * numero_real

print(f'O produto do dobro do primeiro com metade do segundo é {calculo_1}')
print(f'A soma do triplo do primeiro com o terceiro é {calculo_2}')
print(f'O terceiro elevado ao cubo é {calculo_3}')