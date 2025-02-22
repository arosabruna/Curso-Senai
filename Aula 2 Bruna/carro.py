# Calcular desconto para compra de Carro #

valor = 50000

if valor >= 80000:
    valor = valor - valor*0.6

elif valor >= 60000:
    valor = valor - valor*0.5

else: valor = 0



print("Esse é o valor do carro com o desconto" + valor)