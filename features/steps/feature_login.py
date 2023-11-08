from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

base_url = "https://www.saucedemo.com/"

@given("que esteja na página de login")
def acessar_login(context):
    context.web.get(base_url)

@when('preencher "{email}" e "{senha}" corretos')
def preencher_email_senha(context, email, senha):
    context.web.find_element(By.ID, "user-name").clear()
    context.web.find_element(By.ID, "user-name").send_keys(email)
    context.web.find_element(By.ID, "password").clear()
    context.web.find_element(By.ID, "password").send_keys(senha)

@when("clicar no botão de login")
def clicar_login(context):
    context.web.find_element(By.ID, "login-button").click()

@then("deve ser mostrado uma lista de produtos")
def lista_produtos(context):
    try:
        elemento = context.web.find_element(By.ID, "inventory_container")
    except NoSuchElementException:
        raise AssertionError('Elemento não encontrado')



    
