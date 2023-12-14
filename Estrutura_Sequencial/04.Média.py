# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print(f'''{"~"*30}
{"MÉDIA ESCOLAR":^30}
{"~"*30}
Digite as notas dos 4 bimestres para saber a média''')
grade1 = float(input('Nota 1: '))
grade2 = float(input('Nota 2: '))
grade3 = float(input('Nota 3: '))
grade4 = float(input('Nota 4: '))
average = (grade1 + grade2 + grade3 + grade4) / 4

print(f'A sua média é {average}')