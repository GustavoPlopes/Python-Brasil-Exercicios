# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

from modulos_úteis import menu

menu('FORMA OU NÂO UM TRIÂNGULO')
lado1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Agora o tamanho do segundo lado do triângulo: '))
base = float(input('E por ultimo a base do triângulo: '))

if lado1 == lado2 and lado1 == base:
    print('Você tem um triângulo !EQUILÁTERO!')
elif lado1 == lado2 or lado1 == base or lado2 == base :
    print('Você tem um triângulo !ISÓSELES!')
elif lado1 and lado2  != base:
    print('Você tem um triângulo !ESCALENO!')
    