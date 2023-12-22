# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
from módulos_estrutura_sequencial import Modulos_Úteis
from emoji import emojize

# Versão sem módulo
Modulos_Úteis.menu('SALÁRIO COM %DESCONTOS%')
ganho_por_hora = float(input('Digite o valor que ganha por hora: \033[32mR$\033[m'))
tempo_trabalhado = float(input(emojize('Agora digite o :three_o’clock:tempo:three_o’clock: trabalhado: ')))
salario_bruto = ganho_por_hora * tempo_trabalhado
ir = (salario_bruto/100) * 11
inss = (salario_bruto/100) * 8
sindicato = (salario_bruto/100) * 5
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'''{"-"*30}
+ Salário Bruto: R${salario_bruto:.2f}
- IR (11%): R${ir:.2f}
- INSS (8%): R${inss:.2f}
- Sindicato (5%): R${sindicato:.2f}
= Salário Liquido: R${salario_liquido:.2f}
{"-"*30}'''.replace('.', ','))

# Versão com módulo
print('Versão utilizando módulo')
Modulos_Úteis.salario_desconto(ganho_por_hora, tempo_trabalhado)

