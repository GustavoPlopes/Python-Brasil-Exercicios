"""Classe Pessoa:
Crie uma classe que modele uma pessoa: Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa
envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""


class pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self, nova_idade):
        self.idade = nova_idade
        if nova_idade < 21:
            self.altura += 0.05
            print(f'Agora com {nova_idade} anos, {self.nome} tem {self.altura}m de altura')

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


p = pessoa('Gustavo', 15, 1.79, 95)
print(p.__dict__)

p.envelhecer(16)
print(p.__dict__)

p.engordar(2)
print(p.__dict__)

p.emagrecer(1)
print(p.__dict__)

p.crescer(0.05)
print(p.__dict__)

print(f'{p.nome} tem {p.idade} anos, mede {p.altura:.2f}m e pesa {p.peso:.2f}Kg')
