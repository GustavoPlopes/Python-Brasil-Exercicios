"""Classe Conta Corrente: Crie uma classe para implementar uma conta-corrente.

A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.

Os métodos são os seguintes: alterar Nome, depósito e saque, no construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios."""


class conta_corrente:
    def __init__(self, num_conta, nome, saldo):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'Nome alterado com sucesso\n{"~"*40}')

    def depósito(self, dinheiro):
        self.saldo += dinheiro
        print(f'''Deposito: R${dinheiro:.2f}
saldo: R${self.saldo:.2f}'''.replace('.', ','))


    def saque(self, dinheiro):
        self.saldo -= dinheiro
        print(f'''Saque: R${dinheiro:.2f}
Saldo: R${self.saldo:.2f}'''.replace('.', ','))


pessoa = conta_corrente(int(input('Numero da conta? ')), str(input('Seu nome? ')), float(input('Seu saldo? ')))
print(pessoa.__dict__)

while True:
    opç = int(input(f'''{"~"*40}
{"GUSTA BANK":^40}
{"~"*40}
[1] - Alterar nome
[2] - Depósito
[3] - saque 
[4] - Sair
Escolha sua opção>> '''))
    print(f'{"~"*40}')

    if opç == 1:
        pessoa.alterar_nome(str(input('Digite novo nome para alterar: ')).strip().title())
    elif opç == 2:
        pessoa.depósito(float(input('Qual valor deseja depósitar? ')))
    elif opç == 3:
        pessoa.saque(float(input('Qual valor deseja sacar? ')))
    elif opç == 4:
        print(f'''Conta: {pessoa.num_conta}
Nome: {pessoa.nome}
Saldo: R${pessoa.saldo:.2f}
Obrigado e volte sempre !''')
        break



