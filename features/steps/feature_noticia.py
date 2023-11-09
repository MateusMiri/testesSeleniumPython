from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

base_url = "https://www.uol.com.br/esporte/"
manchete = ""

@given("que esteja na página de notícias de Esporte do UOL")
def acessar_login(context):
    context.web.get(base_url)

@when('clicar em uma manchete')
def escolher_manchete(context):
    global manchete
    elemento = context.web.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/a[1]")
    manchete = elemento.text
    elemento.click()

@then("deve ser mostrada a manchete escolhida")
def validar_manchete(context):
    global manchete
    try:
        elemento = context.web.find_element(By.XPATH, "/html/body/div[1]/main/article/div[1]/div[1]/div/div[1]/div/div[2]/div/h1")
        if elemento.text != manchete:
            raise AssertionError("Manchete incorreta exibida")
    except NoSuchElementException:
        raise AssertionError('Manchete não encontrada')


    
