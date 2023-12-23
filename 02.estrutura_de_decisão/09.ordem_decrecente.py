# Faça um Programa que leia três números e mostre-os em ordem decrescente.

from modulos_úteis import menu

números = []
menu('ORDEM DECRECENTE')

for n in range(0, 3):
    número = int(input(f'- Número {n+1}: '))
    números.append(número)

números.sort(reverse=True)
print(f'{"-"*30}')
print('Os números digitados em ordem decrecente são ', end='')    
for i in range(0, 3):
    print(números[i], end=', ' if i != 2 else '.')