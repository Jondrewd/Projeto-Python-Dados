import pandas as pd
import requests
from bs4 import BeautifulSoup


dados = []

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}


def BuscasPreços():
    n=1
    while(n<=19):
        link = ('https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/{}'.format(n))
        news_site = requests.get(link, headers= headers).text
        promo = BeautifulSoup(news_site, 'html.parser')
        produtos = promo.find_all('a', attrs={'class':'product-card--wrapper'})

        for precos in produtos:
            nomes = precos.find('h3', class_='product-title single-line-name')
            preco = precos.find('span', class_='product-button__label').contents[1:4]
            preco = str(preco[0:4])
            preco = preco.replace('<sup class="currency-symbol">', "").replace("</sup>" , "").replace("eu", "").replace('<span class="integer">', "").replace("</span>", "").replace('<span class="decimal">', "").replace(' ,', '')

            dados.append((nomes, preco))            
        df= pd.DataFrame(dados, columns=['Nomes', 'Preço'])
        print(df)
        n+=1

BuscasPreços()