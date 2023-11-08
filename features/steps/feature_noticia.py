# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import *

# # base_url = "https://www.uol.com.br/esporte/"
# base_url = "https?//www.google.com"
# manchete = ""

# @given("que esteja na página de notícias de Esporte do UOL")
# def acessar_login(context):
#     context.web.get(base_url)

# @when('clicar em uma manchete')
# def preencher_email_senha(context):
#     elemento = context.web.find_element(By.XPATH, "/html/body/div[1]/main/article/div[1]/div[1]/div/div[1]/div/div[2]/div/h1").text()
#     manchete = elemento.text()
#     elemento.click()
#     print(1)

# @then("deve ser mostrada a manchete escolhida")
# def lista_produtos(context):
#     try:
#         elemento = context.web.find_element(By.CLASS_NAME, "title")
#         return True if elemento.Text() == manchete else False
#     except NoSuchElementException:
#         raise AssertionError('Manchete não encontrada')
#     print(2)


    
