from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://testpages.eviltester.com/styled/key-click-display-test.html"

@given("que esteja na página de testes de Teclas")
def acessar_site(context):
    context.web.get(base_url)

@when('pressionar e soltar uma tecla')
def clicar_tecla(context):
    elemento = context.web.find_element(By.XPATH, "/html/body")
    elemento.send_keys(Keys.NUMPAD3)

@then("devem ser mostradas as ações de acionamento e desacionamento da tecla")
def validar_acoes_teclas(context):
    try:
        WebDriverWait(context.web, 10).until(EC.presence_of_element_located((By.ID, 'event2')))
        if context.web.find_element(By.ID, 'event1').text != "down 3 99" or context.web.find_element(By.ID, 'event2').text != "up 3 99":
            raise AssertionError("Mapeamento de Ações incorreto")
    except NoSuchElementException:
        raise AssertionError('Elemento não Encontrado')


    
