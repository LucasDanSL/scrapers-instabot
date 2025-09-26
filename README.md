Video da aplicação : https://youtu.be/3exmmuMxQ8c?si=8JogAuqZUkGzTVB_

Scrapers Instabot
Descrição

Scrapers Instabot é um projeto em Python para coletar dados de diferentes fontes na web. Ele possui duas funcionalidades principais:

Scraper de Notícias

Coleta títulos, links e resumos de livros do site Books to Scrape (http://books.toscrape.com/
).

Salva os dados em formato JSON (manchetes.json).

Scraper de Bio do Instagram (Instabot)

Faz login no Instagram de forma automatizada usando Selenium.

Captura nome de usuário e bio de perfis públicos, mantendo apenas o texto visível.

Salva os dados em JSON (bio_instagram.json).

Exemplo de saída:

{
  "perfil": "@computacaounifavip_",
  "bio": "Perfil oficial dos cursos:\n👨‍💻 Ciência da Computação\n👨‍💻 Análise e Desenvolvimento de Sistemas\n📍UniFavip | Wyden"
}


Observação: Para o Instabot funcionar corretamente, é necessário alterar o arquivo .env com seu usuário e senha do Instagram.

Tecnologias Utilizadas

Python 3.10+

Selenium (automação do navegador)

BeautifulSoup (processamento e limpeza de HTML)

Requests (coleta de páginas web)

dotenv (armazenamento seguro de credenciais)

Estrutura do Projeto
scrapers-instabot/
├─ news_scraper.py       # Scraper de notícias  
├─ insta_bot.py          # Scraper de bio do Instagram  
├─ main.py               # Menu interativo  
├─ bio_instagram.json    # Resultado do Instabot  
├─ manchetes.json        # Resultado do scraper de notícias  
├─ .env                  # Usuário e senha do Instagram  
├─ requirements.txt      # Dependências do projeto  
└─ README.md             # Documentação do projeto

Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/scrapers-instabot.git
cd scrapers-instabot


Crie um ambiente virtual:

python -m venv venv


Ative o ambiente virtual:

No PowerShell:

.\venv\Scripts\Activate


No CMD:

venv\Scripts\activate.bat


Instale as dependências:

pip install -r requirements.txt


Crie o arquivo .env na raiz do projeto:

IG_USERNAME=seu_usuario
IG_PASSWORD=sua_senha


Substitua seu_usuario e sua_senha pelos seus dados do Instagram.

Como Executar

Execute o menu principal:

python main.py


Você verá opções:

Escolha uma opção:
1 - Scraper de Notícias
2 - Scraper de Bio Instagram
0 - Sair
Digite a opção:


Digite 1 para coletar notícias.

Digite 2 para coletar nome e bio do Instagram.

Digite 0 para sair.

Os resultados serão salvos nos arquivos manchetes.json e bio_instagram.json, respectivamente.

Exemplo de Código
Leitura de JSON no Python
import json

with open("bio_instagram.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

Exemplo de execução no terminal
python main.py

Observações

Nunca compartilhe seu arquivo .env publicamente, pois contém credenciais.

Você pode rodar o Instabot em modo headless descomentando a linha correspondente em insta_bot.py.

Use um tempo de espera (sleep) entre requisições para não sobrecarregar os sites.
