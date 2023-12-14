# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
from módulos_estrutura_sequencial import Modulos_Úteis

multa = 4.0
Modulos_Úteis.menu('CALCULO DE MULTA DE PESCA')
peso_pesca = float(input('Digite quantos quilos de peixe(s) pescado: '))

if peso_pesca > 50:
    peso_pesca -= 50
    multa *= peso_pesca
    print(f'{"-"*30}')
    print(f'\033[31mJoão Papo-de-Pescador, você excedeu o limite diario de 50KG de pesca, o valor da multa é de '
          f'R${multa:.2f}\033[m')
else:
    print(f'{"-"*30}')
    print('\033[34mJoão Papo-de-Pescador, você está dentro do limite permitido de 50Kg.\033[m')
