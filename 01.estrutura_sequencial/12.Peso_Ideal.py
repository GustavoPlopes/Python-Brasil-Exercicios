# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
from modulos_úteis import menu

menu('PESO IDEAL')
altura = float(input('Digite a sua altura para saber o seu peso ideal: '))
peso_ideal = (72.7 * altura) - 58

print(f'''{"-"*30}
O seu peso ideal é {peso_ideal:.2f}Kg''')