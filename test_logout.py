from selenium import webdriver
from selenium.webdriver.edge.service import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


user = "test11"
email = "test11@gmail.com"
passwd = "test11test11"


def test_logout():
    driver = webdriver.Edge()
    driver.get("https://www.mikenatsu.com/en/login")
    print("Iniciando login automatizado")
    usuario = driver.find_element(By.NAME, "username")
    usuario.send_keys(user)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/logout/1. escribir_nombre.png')   
    clave = driver.find_element(By.NAME, "password")
    clave.send_keys(passwd)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/logout/2. escribir_contraseña.png')   
    clave.send_keys(Keys.ENTER)
    time.sleep(2)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/logout/3. login_completo.png')  
    time.sleep(3)

    click_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/button[2]")
    click_button.click()
    time.sleep(1)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/logout/4. loguot_completo.png')
    time.sleep(10)
    driver.close()
