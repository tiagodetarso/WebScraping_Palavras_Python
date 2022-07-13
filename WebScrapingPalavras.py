from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

navegador = webdriver.Chrome()
url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"

opcao = Options()
opcao.headless = True
navegador.get(url)

conteudo = navegador.find_element(By.XPATH, "//html/body/pre")
html_conteudo = conteudo.get_attribute("outerHTML")

soup = bs(html_conteudo, "html.parser")

lista_palavras = str(soup).split("\n")

Palavras_5letras = []

for palavra in lista_palavras:
    if len(palavra) == 5 and palavra[0].islower():
        Palavras_5letras.append(palavra)

print(Palavras_5letras)

print(len(Palavras_5letras))

navegador.quit()