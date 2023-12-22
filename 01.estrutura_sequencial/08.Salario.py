# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês

ganho_por_hora = float(input('Digite o quanto você recebe por hora trabalha: '))
horas_trabalhadas = float(input('Agora digite quantas horas trabalhadas no mês: '))
salario = ganho_por_hora * horas_trabalhadas
print(f'Seu salario é de > R$ {salario:.2f}')