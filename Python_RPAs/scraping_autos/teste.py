
# Importar as bibliotecas necessárias
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random

# Configurar as opções do Chrome para evitar detecção
chrome_options = Options()

# Modificar o User-Agent para um valor comum
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/90.0.818.56',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/76.0.4017.177'
]

chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')

# Remover recursos de automação que possam ser detectados
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# Iniciar o navegador maximizado para parecer mais natural
chrome_options.add_argument('start-maximized')

# Inicializar o WebDriver com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

# Acessar a página desejada
url = 'https://myanimelist.net/'

driver.get(url)

time.sleep(random.uniform(5, 10))

# last_height = driver.execute_script("return document.body.scrollHeight;")
#
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#
#     new_height = driver.execute_script("return document.body.scrollHeight;")
#     if new_height == last_height:
#         break
#     last_height = new_height
#


# Obter o elemento de corpo da página
body = driver.find_element(
    by=By.TAG_NAME,
    value="body"
)

divs = driver.find_elements(
    by=By.TAG_NAME,
    value="div"
)
print(len(divs))
# Enviar a tecla de seta para baixo
body.send_keys(Keys.ARROW_DOWN)  # Simula a tecla seta para baixo


# Rolar para baixo várias vezes
for _ in range(len(divs)):  # Número de vezes para rolar
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)  # Pequena pausa entre rolagens





