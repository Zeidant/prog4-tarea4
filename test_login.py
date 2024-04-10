from selenium import webdriver
from selenium.webdriver.edge.service import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


user = "test11"
email = "test11@gmail.com"
passwd = "test11test11"


def test_login():
    driver = webdriver.Edge()
    driver.get("https://www.mikenatsu.com/en/login")
    print("Iniciando login automatizado")
    usuario = driver.find_element(By.NAME, "username")
    usuario.send_keys(user)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/login/1. escribir_nombre.png')   
    clave = driver.find_element(By.NAME, "password")
    clave.send_keys(passwd)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/login/2. escribir_contraseña.png')   
    clave.send_keys(Keys.ENTER)
    time.sleep(2)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/login/3. login_completo.png')      
    time.sleep(5)
    driver.close()

test_login()