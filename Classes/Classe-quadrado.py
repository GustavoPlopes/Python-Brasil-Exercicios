class quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, valor):
        self.tamanho_lado = valor

    def retornar_valor_lado(self):
        print(self.tamanho_lado)

    def calcular_área(self, tamanho=0):
        tamanho = self.tamanho_lado
        área = tamanho * tamanho
        print(área)


q1 = quadrado(5)
q1.retornar_valor_lado()
q1.mudar_valor_lado(10)
q1.retornar_valor_lado()
q1.calcular_área()
