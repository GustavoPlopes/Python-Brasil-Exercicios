# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Digite o valor em graus fahrenheit para ser convertido em celcius: '))
celcius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit:.2f}° graus fahrenheit é {celcius:.2f}° graus em celcius ")