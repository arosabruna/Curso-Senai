import requests # Responsável por enviar a requisição
from bs4 import BeautifulSoup #Responsável por tratar a requisição

# class -> feed-post-link

# URL do site 
url = "https://www.buscape.com.br/?og=19220&og=19220&gad_source=1&gclid=EAIaIQobChMIxJLsp6-MjAMVIF5IAB06gRFaEAAYASAAEgKtzvD_BwE"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0: Win64: x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}



# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)

# verificar se deu tudo certo
if resposta.status_code == 200: 
    # código 200 -> sucesso
    # print("Requisição feita com sucesso.")
    # print(resposta.text) # retorno
    #preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as produtos
    produtos = soup.find_all("a", class_="ProductCard_ProductCard_Inner__gapsh")
    print("Celulares abaixo de R$ 3.000 no Buscapé\n")
    for produto in produtos[ : 20]: # Puxar até 20 itens
        item = produto.find("h2")
        preco = produto.find("a", class_="ProductCard_ProductCard_Inner__gapsh")

        if item and preco:
            item = item.text.strip()
            preco = preco.text.strip().replace("R$", "").replace(".", "").replace(",", ".")
            
            try:
                preco = float(preco) # converter em número
                if preco < 3000: # se o item for menos que R$ 3000, ele irá puxa
                    print("f{item} - R$ {preco: .2f}")
            except ValueError:
                pass
else:
    print("Erro ao acessar o site")
    print("Ofertas Buscapé")


