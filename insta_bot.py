import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')
PROFILE = 'computacaounifavip_'

# insta_bot.py
def run_instagram_scraper(username, password, profile):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import time
    import json

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # descomente para rodar sem abrir navegador

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # Login
        driver.get("https://www.instagram.com/accounts/login/")
        user_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pass_input = driver.find_element(By.NAME, "password")
        user_input.clear()
        user_input.send_keys(username)
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.RETURN)
        time.sleep(4)

        # Ignorar "Salvar informações?" ou "Ativar notificações?"
        try:
            not_now = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Agora não') or contains(., 'Not Now') or contains(., 'Não agora')]")
            ))
            not_now.click()
        except Exception:
            pass

        # Acessar perfil
        driver.get(f"https://www.instagram.com/{profile}/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))

        # Capturar bio apenas como texto
        try:
            bio_element = driver.find_element(By.CSS_SELECTOR, "span._ap3a._aaco._aacu._aacx._aad7._aade")
            bio_html = bio_element.get_attribute("innerHTML")
            bio_text = BeautifulSoup(bio_html, "lxml").get_text("\n").strip()  # converte <br> em \n e remove tags
        except Exception:
            bio_text = ""

        # Salvar resultado em JSON
        resultado = {"perfil": f"@{profile}", "bio": bio_text}
        with open("bio_instagram.json", "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)

        print("Bio salva em bio_instagram.json")
        return resultado

    finally:
        time.sleep(2)
        driver.quit()


# Se rodar direto, executa
if __name__ == "__main__":
    run_instagram_scraper(USERNAME, PASSWORD, PROFILE)
