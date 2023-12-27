# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

from modulos_úteis import menu
from datetime import date

menu('DIA DA SEMANA')
semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
dia = int(input('Digite um número de 1 à 7 para saber o dia da semana: '))

if dia > 7:
    print('Valor inválido')
else:
    print(f'O dia da semana é {semana[dia - 1]}')