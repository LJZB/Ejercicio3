from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Petición al navegador
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.ui5cn.com/")

# Espera del navegador
wait = WebDriverWait(driver, 2)

# Registro
my_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div/nav/ul/li[5]/a')))
my_element.click()

my_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/div/aside/a')))
my_element.click()

# Nombre
my_element = driver.find_element(By.ID, "user[first_name]")
my_element.send_keys("Luis")
time.sleep(2)

# Apellido
my_element = driver.find_element(By.ID, "user[last_name]")
my_element.send_keys("Zuluaga")
time.sleep(2)

# Correo
my_element = driver.find_element(By.ID, "user[email]")
my_element.send_keys("javier.zuluaga@udea.edu.co")
time.sleep(2)

# Contraseña
my_element = driver.find_element(By.ID, "user[password]")
my_element.send_keys("5ecur3_P4s5")
time.sleep(2)

# Casilla de aceptación de los términos de usuario
my_element = wait.until(EC.element_to_be_clickable((By.ID, 'user[terms]')))
my_element.click()
time.sleep(2)

my_element.send_keys(Keys.TAB)
my_element.send_keys(Keys.TAB)
my_element.send_keys(Keys.TAB)
my_element.send_keys(Keys.TAB)
my_element.send_keys(Keys.TAB)
time.sleep(2)

my_element.send_keys(Keys.ENTER)

time.sleep(10)

# Cerrar el navegador
driver.quit()