class bola:
    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostrar_cor(self):
        print(self.cor)


b1 = bola('Azul', 8, 'Plástico')
b1.troca_cor('Preto')
b1.mostrar_cor()
