# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

from modulos_úteis import menu

menu('REAJUSTE DE SALÁRIO')
salário = float(input('Digite o valor do seu salário para saber o reajuste: R$'))
aumento = 0
percentual = 0

if salário <= 280:
    aumento = (salário / 100) * 20 
    percentual = '20%'
elif salário > 280 and salário <= 700:
    aumento = (salário / 100) * 15 
    percentual = '15%'
elif salário > 700 and salário <= 1500:
    aumento = (salário / 100) * 10 
    percentual = '10%'
elif salário > 1500:
    aumento = (salário / 100) * 5 
    percentual = '5%'
    
print(f'''{"-"*30}
- Antigo salário: R${salário:.2f}
+ Percentual aplicado: {percentual}
+ Valor do aumento: R${aumento:.2f}
+ Novo salário: R${aumento + salário:.2f}
{"-"*30}'''.replace('.', ','))