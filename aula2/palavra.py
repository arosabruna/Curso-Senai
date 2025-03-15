# Identificar Palavra Palíndroma #

p = input("Escreva uma palavra: ").upper()
p1 = p[::-1]

if p == p1:
  print(f"A palavra {p} é palíndroma.")
else:
  print(f"A palavra {p} não é palíndroma.")