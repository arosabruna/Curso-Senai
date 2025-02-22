import math 

print("Digite o valor A:")
valorA = float(input())



print("Digite o valor B:")
valorB = float(input())



print("Digite o valor C:")
valorC = float(input())




delta = valorB**2 - 4 * valorA * valorC
raiz = math.sqrt(delta)
bhaskara1 = (-valorB - raiz) / (2 * valorA)
bhaskara2 = (-valorB + raiz) / (2 * valorA)



print(delta)
print(bhaskara1)
print(bhaskara2)



