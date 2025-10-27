# 🤖 Scrapers Instabot

🎥 Vídeo da aplicação: [Clique aqui](https://youtu.be/3exmmuMxQ8c?si=8JogAuqZUkGzTVB)

**Descrição curta:**  
Projeto em Python para coletar dados de diferentes fontes na web, com duas funcionalidades principais: raspagem de notícias e coleta de biografias públicas do Instagram.

---

## 📌 Funcionalidades

### 📰 Raspador de Notícias
- Coleta títulos, links e resumos de livros do site [Books to Scrape](http://books.toscrape.com/).  
- Salva os dados no formato JSON: `manchetes.json`.

### 📸 Raspador de Bio do Instagram (Instabot)
- Login automatizado no Instagram usando Selenium.  
- Captura nome do usuário e biografia de perfis públicos (somente texto visível).  
- Salva os dados em JSON: `bio_instagram.json`.

**Exemplo de saída:**
```json
{
  "perfil": "@computacaounifavip_",
  "bio": "Perfil oficial dos cursos:\n👨‍💻 Ciência da Computação\n👨‍💻 Análise e Desenvolvimento de Sistemas\n📍UniFavip | Wyden"
}
```

> ⚠️ Observação: Para funcionar corretamente, é necessário configurar o arquivo `.env` com seu usuário e senha do Instagram.

---

## 🛠️ Tecnologias Utilizadas
- Python 3.10+  
- Selenium (automação do navegador)  
- BeautifulSoup (processamento e limpeza de HTML)  
- Requests (coleta de páginas web)  
- python-dotenv (armazenamento seguro de credenciais)

---

## 🏗 Estrutura do Projeto

```
scrapers-instabot/
├─ news_scraper.py       # Scraper de notícias
├─ insta_bot.py          # Scraper de bio do Instagram
├─ main.py               # Menu interativo
├─ bio_instagram.json    # Resultado do Instabot
├─ manchetes.json        # Resultado do scraper de notícias
├─ .env                  # Usuário e senha do Instagram
├─ requisitos.txt        # Dependências do projeto
└─ README.md             # Documentação
```

---

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/scrapers-instabot.git
cd scrapers-instabot
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**No PowerShell:**
```powershell
.env\Scripts\Activate
```

**No CMD:**
```cmd
venv\Scriptstivar.bat
```

4. Instale as dependências:
```bash
pip install -r requisitos.txt
```

5. Crie o arquivo `.env` na raiz do projeto:
```
IG_USERNAME=seu_usuario
IG_PASSWORD=sua_senha
```

> Substitua `seu_usuario` e `sua_senha` pelos seus dados do Instagram.

---

## 🚀 Como Executar

Execute o menu principal:
```bash
python main.py
```

Você verá opções:

```
Escolha uma opção: 
1 - Scraper de Notícias 
2 - Scraper de Bio Instagram 
0 - Sair
```

- Digite `1` para coletar notícias.  
- Digite `2` para coletar nome e bio do Instagram.  
- Digite `0` para sair.

Os resultados serão salvos em `manchetes.json` e `bio_instagram.json`.

---

## 📄 Exemplo de leitura de JSON em Python
```python
import json

with open("bio_instagram.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```

---

## ⚠️ Observações

- Nunca compartilhe o arquivo `.env` publicamente, pois contém suas credenciais.  
- Você pode rodar o Instabot no modo **headless** descomentando a linha correspondente em `insta_bot.py`.  
- Use `sleep` entre requisições para não sobrecarregar os sites.  

---

## 💡 Aprendizados

- Automação web com Selenium  
- Raspagem e processamento de dados com BeautifulSoup  
- Manipulação de JSON em Python  
- Boas práticas de segurança com `.env`  
- Controle de fluxo e menu interativo em Python  
