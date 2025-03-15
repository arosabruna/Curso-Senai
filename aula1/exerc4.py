# Conversor de Temperatura

"""
Solicite ao usuário para fornecer uma temperatura em graus
Converta essa temperatura em Fahrenhit
"""

print("Conversor de Temperatura")


print("digite a temperatura em Graus")
Graus = float(input ())

m = 1.8
s = 32

resultado = (Graus * m) + s

print("essa é a temperatura em Fahrenhit: ", resultado)
