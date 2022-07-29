
from calendar import c
import pyautogui as pyauto
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import io
import os
username = 'teste'
password = 'teste2'

try:
    #ocultar mensagens do webdriver
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--incognito")
    # options.add_argument("--headless") #oculto
    #iniciar driver para o Chrome
    # driver = webdriver.Chrome(chrome_options=options)
    #f = io.open(os.path.join(pastaAtual, 'configportal'), mode='r', encoding='utf-8')
   # data = f.read()
   # username = data.split(';')[0]
    #password = data.split(';')[1]
    driver = webdriver.Chrome()
    #fazer login
    driver.get("https://discord.com/channels/767449676206178347/812088815207579658")
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    # para dar um tecla TAB sem pyautogui
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(Keys.TAB)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
    
except Exception as ex:
    # gravar log de erro {}.format(ex)
    exit()

pyauto.hotkey('ctrl', 'f')


