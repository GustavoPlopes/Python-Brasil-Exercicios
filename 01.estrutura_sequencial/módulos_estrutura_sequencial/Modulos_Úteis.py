def menu(msg):
    print(f'''{"-"*30}
{f"{msg}":^30}
{"-"*30}''')


def salario_desconto(ganho_por_hora, tempo_trabalhado):
    salario_bruto = ganho_por_hora * tempo_trabalhado
    ir = (salario_bruto / 100) * 11
    inss = (salario_bruto / 100) * 8
    sindicato = (salario_bruto / 100) * 5
    salario_liquido = salario_bruto - ir - inss - sindicato
    print(f'''{"-" * 30}
+ Salário Bruto: R${salario_bruto:.2f}
- IR (11%): R${ir:.2f}
- INSS (8%): R${inss:.2f}
- Sindicato (5%): R${sindicato:.2f}
= Salário Liquido: R${salario_liquido:.2f}
{"-" * 30}'''.replace('.', ','))