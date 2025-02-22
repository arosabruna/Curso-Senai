print("Bem vindo a RLCars")


print("Digite um veiculo:")
veiculo = input()

print("Digite o preço deste veiculo: ")
preco = float(input())


mantem = preco * 1000

if mantem >= 80000:
    precoVeiculo = mantem * 0.60
    print("Desconto aplicado de 60% aplicado:", f"{precoVeiculo:.2f}" )
elif mantem >= 50000 and mantem < 80000:
    precoVeiculo = mantem * 0.30
    print("Desconto de 30% aplicado", f"{precoVeiculo:.2f}")
elif mantem < 50000:
    print("Sem desconto, mantém:", f"{mantem:.2f}")

