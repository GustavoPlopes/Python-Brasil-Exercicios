# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from modulos_úteis import menu
from time import sleep

menu('EQUAÇÃO DO SEGUNDO GRAU')

while True:
    a = int(input('Digite o valor de "a": '))
    if a == 0:
        print('Sua equação não é do segundo grau, programa sendo encerrado', end='')
        break
    b = int(input('Digite o valor de "b": '))
    if b < 0:
        print('Sua equação não é do segundo grau, programa sendo encerrado', end='')
        break
    c = int(input('Digite o valor de "c": '))
    
    

sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
