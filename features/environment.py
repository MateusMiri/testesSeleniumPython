from selenium import webdriver

def before_all(context):
    opcoes = webdriver.ChromeOptions()
    # opcoes.add_argument('--no-sandbox')
    # opcoes.add_argument('--disable-gpu')
    # opcoes.add_argument('--headless')
    opcoes.add_argument('--disable-dev-shm-usage')
    opcoes.add_argument('--allow-running-insecure-content')
    opcoes.add_argument('--ignore-certificate-errors')
    context.web = webdriver.Chrome(options=opcoes)


def after_step(context, step):
    print()

def after_all(context):
    context.web.quit()
    
