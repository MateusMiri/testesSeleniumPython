from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time

base_url = "https://gauchazh.clicrbs.com.br/esportes/ultimas-noticias/"
manchete = ""

@given("que esteja na página de notícias da Gaúcha ZH")
def acessar_site(context):
    context.web.get(base_url)

@when('clicar na categoria Copa do Brasil')
def selecionar_categoria(context):
    global manchete
    elemento = context.web.find_element(By.XPATH, '//*[@id="hottopics-slider"]/div[6]')
    manchete = elemento.text
    elemento.click()

@then("devem ser mostradas notícias de acordo com a classificação escolhida")
def valida_manchete(context):
    global manchete
    try:
        time.sleep(2) # o XPATH também existe na tela anterior a esta, então aguardamos 2 segundos até ele sofrer a alteração de seu valor interno
        elemento = context.web.find_element(By.XPATH, '//*[@id="gzh-all"]/div/header/div/div[1]/div/h1')
        
        if elemento.text != manchete:
            raise AssertionError("Manchete incorreta exibida")
    except NoSuchElementException:
        raise AssertionError('Manchete não encontrada')

    
