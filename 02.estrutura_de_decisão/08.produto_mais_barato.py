# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

from modulos_úteis import menu

mais_barato = 0
menu('PRODUTO MAIS BARATO')
produto1 = float(input('Informe o preço de três produtos para saber o valor do mais barato\nProduto 1: '))
produto2 = float(input('Produto 2: '))
produto3 = float(input('Produto 3: '))

if produto1:
    mais_barato = produto1
    if produto2 < mais_barato:
        mais_barato = produto2
    elif produto3 < mais_barato:
        mais_barato = produto3

print(f'{"-"*30}')       
print(f'O produto mais barato custa R${mais_barato:.2f}')

# Versão com função
print(f'\nO produto mais barato custa R${min(produto1, produto2, produto3):.2f}')

