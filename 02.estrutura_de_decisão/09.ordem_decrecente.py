# Faça um Programa que leia três números e mostre-os em ordem decrescente.

from modulos_úteis import menu

números = []
menu('ORDEM DECRECENTE')
# número1 = int(input('- Número 1: '))
# número2 = int(input('- Número 2: '))
# número3 = int(input('- Número 3: '))
for n in range(0, 3):
    número = int(input(f'- Número {n+1}: '))
    números.append(número)


print(f'{"-"*30}')
print('Os números digitados em ordem decrecente são ', end='')    

print(f'{números}')