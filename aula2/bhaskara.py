 # Calcular o Delta e aplicar Bhaskara #


a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = b**2 - 4*a*c

x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)

print(x1, x2)
