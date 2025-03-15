
# Números pares em um intervalo

"""
Solicite dois números inteiros ao usuário
Representando o inicio e o fim do intervalo
Mostre todos os números pares nesse intervalo
(incluindo limite inicial e final, se forem pares)
"""

# print("Números pares em um intervalo")


# print("Digite um número de inicio")
# inicio = int(input ())

# print("Digite um número de fim")
# fim = int(input ())

# for y in range(inicio, fim + 1):
#     if y % 2 == 0:
#         print("o número é par: ", y)


    
print("Digite um numero")
a=int (input())

resto = a % 2

print("Digite um numero")
b=int (input())

if resto == 0:
    for y in range(a, b, +2):
        print(y)
else:
    for y in range(a, b, +2):
        print(y+1)

     

   


   
    

