# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#    Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

from modulos_úteis import menu

menu('FOLHA DE PAGAMENTO')
valor_da_hora = float(input('Digite o valor da sua hora trabalhada: R$'))
horas_trabalhadas = float(input('Quantidade de horas trablhadas no mês: '))
salário = horas_trabalhadas * valor_da_hora
ir = 0
porcentagem_ir = 0
inss = (salário/100) * 10
fgts = (salário/100) * 11
total_descontos = ir + inss

if salário > 900 and salário <= 1500:
    ir = (salário/100) * 5
    porcentagem_ir = 5
elif salário > 1500 and salário <= 2500:
    ir = (salário/100) * 10
    porcentagem_ir = 10
elif salário > 2500:
    ir = (salário/100) * 20
    porcentagem_ir = 20

    

print
print(f'''{"-"*60}
Salário Bruto: ({horas_trabalhadas} * R${valor_da_hora:.2f})\t: R${salário:.2f}
      (-) IR ({porcentagem_ir}%)\t\t: R${ir:.2f}
      (-) INSS (10%)\t\t: R${inss:.2f}
      FGTS (11%)\t\t: R${fgts:.2f}
      Total de descontos\t: R${total_descontos:.2f}
      Salário Liquido\t\t: R${salário - total_descontos:.2f}
{"-"*60}'''.replace('.', ','))
