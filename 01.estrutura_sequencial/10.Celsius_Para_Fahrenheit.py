# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

celsius = float(input('Digite o valor da temperatura em Celcius para transformar em Fahrenheit: '))
fahrenheit = celsius * 1.8 + 32
print(f'{celsius:.2f}° graus celsius é {fahrenheit:.2f}° em fahrenheit')