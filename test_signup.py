from selenium import webdriver
from selenium.webdriver.edge.service import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


user = "test13"
email = "test13@gmail.com"
passwd = "test13test13"


def test_sign_up():
    driver = webdriver.Edge()
    driver.get("https://www.mikenatsu.com/en/register")
    print("Iniciando registro automatizado")
    usuario = driver.find_element(By.NAME, "username")
    usuario.send_keys(user)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/sign_up/1. escribir_nombre.png') 

    correo = driver.find_element(By.NAME, "email")
    correo.send_keys(email)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/sign_up/2. escribir_email.png') 

    clave = driver.find_element(By.NAME, "password")
    clave.send_keys(passwd)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/sign_up/3. escribir_contraseña.png') 
    clave.send_keys(Keys.ENTER)
    time.sleep(3)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/sign_up/4. registro_completo.png') 
    time.sleep(5)
    driver.close()