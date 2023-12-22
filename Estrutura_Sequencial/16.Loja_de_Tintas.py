# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from módulos_estrutura_sequencial import Modulos_Úteis

Modulos_Úteis.menu('LOJA DE TINTAS')

litros = 0
litros_totais = 0
latas = 0
preço_total = 0
tamanho_area = float(input('Qual o tamanho da area a ser pintada em metros quadrados? '))

while True:
    if tamanho_area >= 3:
        litros += 1
        litros_totais += 1
        tamanho_area -= 3
        if litros >= 18:
            preço_total += 80
            latas += 1
            litros -= 18
    else:
        break

print(f'{"-"*75}')
if preço_total < 80:
    print(f'O tamanho da area a ser pintada usara {litros}L de tinta, vendemos apenas latas com 18L de tinta, caso '
          f'queria comprar mesmo assim o valor é de R$80,00')
else:
    print(f'O tamanho da area a ser pintada usara {litros_totais}L de tinta, e precisara de {latas}',
          'lata' if latas <= 1 else 'latas', f'\nValor total: R${preço_total:.2f}\n{"-"*75}')