import csv

# Criar e escrever um arquivo TXT   
# W -> Whrite -> Escrita    
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome, Idade, Cidade\n")
    arquivo.write("Alberto, 92, Chique-Chique/BA\n")
    arquivo.write("Arthur, 28, Arrail/RJ\n")
    arquivo.write("Matheus, 28, Cotia/SP\n")

    # Ler o conteudo
    # r -> Read -> Ler
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Conteudo do Arquivo txt:")
    print(arquivo.read())

# Criando arquivo CSV
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Carlos", "32", "Santa Isabel"],
    ["Tulio", "53", "Carapicuiba"],
    ["Rafael", "18", "Taboão da Serra"]
]

# Criar aquivo CSV
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

# Ler o arquivo csv
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo)
    print("\nConteúdo do Arquivo CSV")
    for linha in leitor:
        print(linha)
