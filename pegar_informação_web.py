
from smtpd import DebuggingServer
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from time import sleep
import io
import os

pastaAtual = os.path.dirname(os.path.abspath(__file__))
driverpath = pastaAtual.split('\\')[0]+ '\\'+pastaAtual.split('\\')[1]+ '\\'+'chromedriver.exe'
arquivo = open(os.path.join(pastaAtual, 'noticias.txt'),'a', encoding='utf-8')

navegador = webdriver.Chrome(driverpath)
navegador.get('https://veja.abril.com.br/')
sleep(3)
navegador.find_element(By.XPATH, '/html/body/header/div/div/div[3]/button/i').click()
sleep(2)
navegador.find_element(By.XPATH, '/html/body/header/div/div/div[3]/form/input[1]').send_keys('tecnologia')
sleep(1)
navegador.find_element(By.XPATH, '/html/body/header/div/div/div[3]/form/input[1]').send_keys(Keys.ENTER)
sleep(3)

lista_noticias = []

lista_noticias.append('/html/body/div[2]/section/div/div[1]/section/div/div[1]/div/div[1]/a[2]/h2')

n1 = '/html/body/div[2]/section/div/div[1]/section/div/div[1]/div/div[1]/a[2]/h2'
n2 = '/html/body/div[2]/section/div/div[1]/section/div/div[2]/div/div[1]/a[2]/h2'
n3 = '/html/body/div[2]/section/div/div[1]/section/div/div[3]/div/div[1]/a[2]/h2'
n4 = '/html/body/div[2]/section/div/div[1]/section/div/div[4]/div/div[1]/a[2]/h2'
n5 = '/html/body/div[2]/section/div/div[1]/section/div/div[5]/div/div[1]/a[2]/h2'

lista_noticias = [n1, n2, n3, n4, n5]

for noticia in lista_noticias:
    noti = navegador.find_element(By.XPATH, noticia).text
    arquivo.write(noti)
    arquivo.write("\n")

arquivo.close()