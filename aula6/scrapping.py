import requests # Responsável por enviar a requisição
from bs4 import BeautifulSoup #Responsável por tratar a requisição

# class -> feed-post-link

# URL do site 
url = "https://paulofigueiredoshow.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0: Win64: x64) Applewebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}



# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)

# verificar se deu tudo certo
if resposta.status_code == 200: 
    # código 200 -> sucesso
   #  print("Requisição feita com sucesso.")
    # print(resposta.text) # retorno
    #preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as noticias
    noticias = soup.find_all("div", class_="elementor-post__text")
    # print(noticias)
    print("Noticias Paulo Figueiredo Show")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1}. {noticia.text.strip()}) ")

