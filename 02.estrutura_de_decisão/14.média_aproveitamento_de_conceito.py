# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

from modulos_úteis import menu

menu('APROVADO OU REPROVADO')
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
média = (nota1 + nota2) / 2
Aproveitamento = ""

print(f'''{"-"*30}
Suas notas foram {nota1} e {nota2}
Média: {média}''')
if média >= 9:
    Aproveitamento = 'A'
    print(f'''Conceito: "{Aproveitamento}"
Você foi aprovado!''')
elif média >= 7.5 and média < 9:
    Aproveitamento = 'B'
    print(f'''Conceito: "{Aproveitamento}"
Você foi aprovado!''')
elif média >= 6 and média < 9:
    Aproveitamento = 'C'
    print(f'''Conceito: "{Aproveitamento}"
Você foi aprovado!''')
elif média >= 4 and média < 6:
    Aproveitamento = 'D'
    print(f'''Conceito: "{Aproveitamento}"
Você foi REPROVADO!''')
elif média == 0 and média < 4:
    Aproveitamento = 'E'
    print(f'''Conceito: "{Aproveitamento}"
Você foi REPROVADO!''')