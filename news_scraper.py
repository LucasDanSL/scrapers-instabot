# news_scraper.py
# Importações necessárias
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time

# URL base do site que vamos scrapear
BASE = 'http://books.toscrape.com/'

# Função para obter a descrição do livro
def get_book_description(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()  # garante que a requisição deu certo
    s = BeautifulSoup(r.text, 'lxml')
    desc_header = s.find('div', id='product_description')
    if desc_header:
        p = desc_header.find_next_sibling('p')
        if p:
            return p.get_text(strip=True)
    return ''  # se não houver descrição

# Função principal que faz o scraping da página inicial
def scrape_books_homepage():
    r = requests.get(BASE, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')
    resultados = []
    for pod in soup.select('article.product_pod'):
        a = pod.h3.a
        title = a['title'].strip()
        href = a['href']
        link = urljoin(BASE, href)
        resumo = get_book_description(link)
        resultados.append({
            "titulo": title,
            "link": link,
            "resumo": resumo
        })
        time.sleep(0.5)  # para não sobrecarregar o servidor
    return resultados

# Executa o scraping e salva em JSON
if __name__ == "__main__":
    data = scrape_books_homepage()
    with open('manchetes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Salvo {len(data)} itens em manchetes.json")
