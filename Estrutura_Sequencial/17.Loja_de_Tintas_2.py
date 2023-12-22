# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias.
from módulos_estrutura_sequencial import Modulos_Úteis

litros = 0
latas_18l = 0
galoes = 0
valor_latas = 0
valor_galoes = 0
Modulos_Úteis.menu('LOJA DE TINTAS')
metros_quadrados = float(input('\033[1;34mDigite o tamanho o tamanho da área em metros quadrados:\033[m '))
print(f'{"-"*60}')

while True:
    if metros_quadrados >= 6:
        litros += 1
        metros_quadrados -= 6
        if litros >= 18:
            latas_18l += 1
            valor_latas += 80
            litros -= 18
    elif litros >= 3.6:
        galoes += 1
        valor_galoes += 25
        litros -= 3.6
    else:
        break

if latas_18l >= 1 and galoes == 0:
    print(f'Você vai precisar de {latas_18l}', 'lata' if latas_18l == 1 else 'latas', f'de 18L\nValor total: '
                                                                                      f'R${valor_latas:.2f} ')
elif galoes >= 1 and latas_18l == 0:
    print(f'Você vai precisar de {galoes}', 'galão' if galoes == 1 else 'galões', f'de 3,6L\nValor total: '
                                                                                  f'R${valor_galoes:.2f}')
elif latas_18l >= 1 and galoes >= 1:
    if litros < 18 > 3.6:
        latas_18l += 1
        valor_latas += 80
    elif litros < 3.6:
        galoes += 1
        valor_galoes += 25
    print(f'Você vai precisar de {latas_18l}', 'lata' if latas_18l == 1 else 'latas', f'de 18L e de {galoes}', 'galão'
    if galoes == 1 else 'galões', f'de 3,6L\nValor total: R${valor_latas + valor_galoes:.2f} ')