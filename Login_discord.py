# Importar todos as bibliotecas/modulos q vou usar 
from importlib.resources import path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
options = webdriver.ChromeOptions()
options.add_argument("--icognito")

# exemplo de utilizacao split e direcionando para um unico exe do chromedriver
driverpath = pastaAtual.split('\\')[0]+ '\\'+pastaAtual.split('\\')[1]+ '\\'+'chromedriver.exe'

# declarar e iniciar o navegador
# navegador = webdriver.Chrome(path=driverpath)
# fazer login no discord 
navegador = webdriver.Chrome(driverpath)
navegador.get("https://discord.com/channels/767449676206178347/812088815207579658")
sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
navegador.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
sleep(15)
#apos isso entra em captcha mas login feito e tirado email e senha do txts