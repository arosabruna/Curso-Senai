for x in range(1,11):
    for contador in range(1,11):
        print(f"{x}" , "x" , * f"{contador}", "=", x * contador)
        # print(f"{x}" * contador)


print("Digite um numero: ")
numero = int(input())
for j in range(numero):
    for i in range(1,11):
        print(f"{numero}", "x", * f"{i}")





print("Digite um numero: ")
numero2 = int(input())
for j in range(numero2, 11):
     print(f"{numero2}", "x", * f"{j}", "=" , numero2 * j)