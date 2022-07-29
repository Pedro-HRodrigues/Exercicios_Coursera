# Importar todos as bibliotecas/modulos q vou usar 
from importlib.resources import path
from selenium.webdriver.common.by import By
from selenium import webdriver 
from time import sleep
import io
import os

# declarar a variavel pasta atual pra extrair informação do txt
pastaAtual = os.path.dirname(os.path.abspath(__file__))

# pegar login e senha do arquivo 
f = io.open(os.path.join(pastaAtual, 'Dadosdisc'), mode='r', encoding='utf-8')
data = f.read()
username = data.split(';')[0]
password = data.split(';')[1]

# declarando options pra rodar crome em modo anonimo
#options = webdriver.ChromeOptions()
#options.add_argument("--icognito")

# declarar e iniciar o navegador 
# driverpath = os.path.join(pastaAtual, 'chromedriver.exe')
# navegador = webdriver.Chrome(path=driverpath)
navegador = webdriver.Chrome()
navegador.get()