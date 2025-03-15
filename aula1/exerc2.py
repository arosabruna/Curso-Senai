
# Verificar se é ímpar ou par 

"""
Digite um número inteiro
verifique se o número é ímpar ou par
Escreva a mensagem correspondente
"""

print("Digite um numero")
numero = int(input())

resto = número % 2 # 10 / 2 = 0
resto = número != 2


if numero % 2 == 0:
    print("O numero", numero, "é par")
else:
   print("O numero", numero, "é ímpar")