# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

altura = float(input('Digite a altura do quadrado para saber o dobro da sua area: '))
base = float(input('Agora a base: '))
dobro_area = (altura * base) * 2
print(f'O dobro da sua area é > {dobro_area}')