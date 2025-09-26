# main.py
import json
from news_scraper import scrape_books_homepage       # Scraper de livros
from insta_bot import run_instagram_scraper, USERNAME, PASSWORD, PROFILE  # Bot Instagram

def run_news_scraper():
    print("Executando Scraper de Notícias...")
    data = scrape_books_homepage()
    with open('manchetes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Salvo {len(data)} itens em manchetes.json")
    print(json.dumps(data, indent=4, ensure_ascii=False))

def run_instagram_bot():
    print("Executando Scraper de Bio Instagram...")
    resultado = run_instagram_scraper(USERNAME, PASSWORD, PROFILE)
    with open('bio_instagram.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    print("Bio salva em bio_instagram.json")
    print(json.dumps(resultado, indent=4, ensure_ascii=False))

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Scraper de Notícias")
        print("2 - Scraper de Bio Instagram")
        print("0 - Sair")
        escolha = input("Digite a opção: ")

        if escolha == "1":
            run_news_scraper()
        elif escolha == "2":
            run_instagram_bot()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
