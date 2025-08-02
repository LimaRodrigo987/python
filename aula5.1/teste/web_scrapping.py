# requisiçoes para os sites
import requests
# traduzir a resposta
from bs4 import BeautifulSoup

# url para acesso
url= "https://g1.globo.com/"

# fazendo busca do requisição HTTP
resposta = requests.get(url)

# verificar se a requisicao deu certo
if resposta.status_code ==200:
    # 200 até 299 status  -> OK

    # traduzir a resposta - HTML5 e CSS3
    soup = BeautifulSoup(resposta.text,"html.parser")
    
    # print(soup) # vai escrever o html do site

    # encontrar todas as noticias
    noticias = soup.find_all("a",class_="feed-post-link")

    print("Últimas noticias do G1:")
    # percorrendo todas as noticias
    for index, noticia in enumerate(noticias):
       # escrevendo cada noticia
        print(f"{index+1}.{noticia.text}")