# Importar as bibliotecas necessárias
import requests
from elements_actions import SeleniumElementsActions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random


chrome_options = Options()

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
# url = 'https://www.webmotors.com.br/carros-usados/estoque?lkid=1000'
url = 'https://www.icarros.com.br/comprar/usados?reg=city'

driver.get(url)

page_source = driver.page_source


progress_bar = driver.find_element(
    by=By.TAG_NAME,
    value='progress',
)


value = progress_bar.get_attribute("max")
print(value)




soup = BeautifulSoup(page_source, 'html.parser')

names = soup.find_all('p', class_ = 'label__primary ids_textStyle_label_medium_bold')

for name in names:
    print(name.text)
# time.sleep(random.uniform(8, 10))
#
# body = driver.find_element(
#     by=By.TAG_NAME,
#     value="body"
# )
#
# divs = driver.find_elements(
#     by=By.TAG_NAME,
#     value="div"
# )
# print(len(divs))
#
# body.send_keys(Keys.ARROW_DOWN)
#
#
# # Rolar para baixo várias vezes
# for _ in range(28):  # Número de vezes para rolar
#     body.send_keys(Keys.ARROW_DOWN)
#     time.sleep(2)  # Pequena pausa entre rolagens
#
#
# page_source = driver.page_source
# soup = BeautifulSoup(page_source, 'html.parser')
#
# divs = soup.find_all('div', class_='sc-jqCOkK hFyVNd')
#
# for div in divs:
#
#     print(div.find_all('h2', class_='sc-hqyNC Vropq'))
#     print(div.find_all('strong', class_='sc-cJSrbW eckRoT'))
#
# driver.quit()



# Simular comportamento humano com atrasos aleatórios






