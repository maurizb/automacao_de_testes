import time
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions

# Configurar o WebDriver para o Chrome no Windows
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

def testa():
    # localiza o HTML na mesma pasta do script usando pathlib
    file_path = pathlib.Path(__file__).parent.resolve()
    driver.get(f"file:////{file_path}/sample-exercise_.html")

    # localiza e clica no botão "generate"
    driver.find_element(By.NAME, "generate").click()

    # espera que o código gerado possa ser visto e bota ele na variavel codigo
    espera = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "my-value"))
    )
    codigo = espera.text

    # coloca no campo de texto o código capturado
    campo_texto = driver.find_element(By.ID, "input")
    campo_texto.clear()
    campo_texto.send_keys(codigo)

    # clica no botão "test"
    driver.find_element(By.NAME, "button").click()

    # fecha o alerta done
    alerta = Alert(driver)
    alerta.accept()

    # verifica a mensagem exibida
    mensagem = driver.find_element(By.ID, "result").text
    mensagem_esperada = f"It works! {codigo}!"

    #valida se teste passou ou falhou
    if mensagem == mensagem_esperada: 
        print("Teste OK ✔!")
    else:
        print("Teste falhou ❌!")

# executa o teste 3x por pedido do professor
for a in range(3):
    testa()
    time.sleep(3)  

# fecha o chrome
driver.quit()