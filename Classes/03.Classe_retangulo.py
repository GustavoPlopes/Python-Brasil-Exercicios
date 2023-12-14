"""Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de
um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
rodapés necessárias para o local."""


class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor_lados(self, valor1, valor2):
        self.base = valor1
        self.altura = valor2

    def retornar_valor(self):
        print(self.base, self.altura)

    def calculo_área(self):
        área = self.base * self.altura
        return área

    def calculo_perimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        return perimetro


cerâmica = 22.5
cont = 0
x = retangulo(base=float(input(f'''\033[1;34m{"~" * 40}
{"CALCULADORA DE PISO E RODAPÉ":^40}
{"~" * 40}\033[m
Digite a largura do local >> ''')), altura=float(input('Agora a altura >> ')))
print(f'Sua área é de {x.calculo_área()}m² e o perímetro {x.calculo_perimetro()}m ')
