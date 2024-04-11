from selenium import webdriver
from selenium.webdriver.edge.service import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


user = "test15"
email = "test12@gmail.com"
passwd = "test12test12"

def sign_up():
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
    time.sleep(20)
    driver.close()

def login():
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
    time.sleep(10)
    driver.close()

def create_room():
    login()

    click_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/button")    
    click_button.click()
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/create_room/4. click_create_room.png')  
    room_name = driver.find_element(By.NAME, "name")
    room_name.send_keys("room10")
    room_name.send_keys(Keys.ENTER)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/create_room/5. room_name.png')  
    time.sleep(3)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/create_room/6. room_created.png')      
    time.sleep(3)
    driver.close()

def delete_room():
    login()

    click_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/button[3]")
    click_button.click()
    body = driver.find_element(By.XPATH, "/html/body")    
    body.screenshot('screenshots/delete_room/4. clic_para_confirmar.png')    
    time.sleep(2)
    confirm_delete = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/button[2]")
    confirm_delete.click()
    time.sleep(1)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/delete_room/5. despues_confirmar.png')    
    time.sleep(10)
    driver.close()

def logout():
    login()

    click_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/button[2]")
    click_button.click()
    time.sleep(1)
    body = driver.find_element(By.XPATH, "/html/body")
    body.screenshot('screenshots/logout/4. loguot_completo.png')
    time.sleep(10)
    driver.close()