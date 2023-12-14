# Faça um Programa que peça dois números e imprima a soma.
number1 = int(input(f'''{"="*30}
{"+SOMA+":^30}
{"="*30}
Digite o primeiro numero da soma: '''))
number2 = int(input('Agora o segundo: '))

print(f'{number1} + {number2} = {number1+number2}')