# Calculadora IMC

""" 
Solicite o peso em kg e altura do usuario em metros
calcule o IMC ( Indice de Massa Corporal )
Peso / (Altura * Altura)

exibir o IMC 
"""

print("Calculadora de IMC")
print("digite o peso")
peso = float(input ())

print("digite a altura")
altura = float(input ())

resultado = peso / (altura * altura)

print("esse é o seu IMC: ", resultado)

