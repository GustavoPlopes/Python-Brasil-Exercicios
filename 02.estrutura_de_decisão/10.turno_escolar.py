# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

from modulos_úteis import menu

menu('TURNO ESCOLAR')
turno = str(input('''Qual seu turno escolar?
- [M] Matutino
- [V] Vespertino
- [N] Noturno
Escolha uma letra para sua opção >>> ''')).strip().upper()

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor invalido, digite apenas M,V ou N.')