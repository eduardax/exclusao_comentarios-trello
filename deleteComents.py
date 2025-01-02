pip install selenium pandas webdriver-manager chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
#options.add_argument('--headless')


driver = webdriver.Chrome(options=options)

driver.get("https://trello.com/login")

time.sleep(10) 
email_input = driver.find_element(By.ID, "username")
email_input.send_keys("email@email.com") 
email_input.send_keys(Keys.RETURN)

time.sleep(10)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)

driver.get("https://trello.com/c/D1opORge/card")

time.sleep(15)

comentario_especifico = "Estarei fora entre os dias 20/12/2024 a 02/01/2025. "

comentarios = driver.find_elements(By.CSS_SELECTOR, ".X8WOA764yXoFYj")

for comentario in comentarios:
    print(comentario.find_element)
    try:

        if comentario_especifico in comentario.text:

            botao_excluir = comentario.find_element(By.XPATH, '//div[@class="PxL_3a0PSiOjGx"]//a[text()="Excluir"]')
            botao_excluir.click()

            WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, '//h2[text()="Excluir Comentário?"]'))
            )
            
            botao_excluir_comentario = driver.find_element(By.XPATH, '//button[text()="Excluir Comentário"]')
            botao_excluir_comentario.click()

            print("Comentário excluído com sucesso!")
            time.sleep(5)  
    except Exception as e:
        print(f"Erro ao excluir comentário: {e}")


time.sleep(5)
driver.quit()
