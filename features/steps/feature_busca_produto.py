from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.magazineluiza.com.br/"

@given("que esteja na página inicial da Magalu")
def acessar_login(context):
    context.web.get(base_url)

@when('preencher "{produto}" na barra de pesquisa')
def preencher_busca(context, produto):
    context.web.find_element(By.ID, "input-search").clear()
    context.web.find_element(By.ID, "input-search").send_keys(produto)

@when("clicar para pesquisar")
def clicar_pesquisar(context):
    context.web.find_element(By.ID, "input-search").send_keys(Keys.ENTER)

@then('deve ser exibida uma lista com "{produto}" de acordo com a pesquisa')
def lista_produtos(context, produto):
    try:
        WebDriverWait(context.web, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[1]/div/h1')))
        elemento = context.web.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[1]/div/h1').get_attribute('textContent')
        return True if elemento == produto else False
    except NoSuchElementException:
        raise AssertionError('Resultados não condizentes')



    
