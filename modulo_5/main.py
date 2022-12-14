#%%
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys
#%%
cep = sys.argv[1]
    #%%
if cep:
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(ChromeDriverManager().install())

    link = "https://buscacepinter.correios.com.br/app/endereco/index.php"

    browser.get(link)

    browser.maximize_window()
    time.sleep(3)
    #%%

    cep = browser.find_element(By.NAME, 'endereco')
    cep.clear()
    cep.send_keys('29192-278')

    #%%
    cx_selecao = browser.find_element(By.NAME, 'tipoCEP').click()

    cx_selecao = browser.find_element(By.XPATH, '//*[@id="tipoCEP"]/optgroup/option[1]').click()

    #%%
    clear_cx_selecao = browser.find_element(By.XPATH,'//*[@id="resultado"]').click()

    search = browser.find_element(By.ID,'btn_pesquisar').click()

    # %%

    logradouro = browser.find_element(By.XPATH,'/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]').text
    bairro = browser.find_element(By.XPATH,'/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]').text
    localidade = browser.find_element(By.XPATH,'/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]').text

    browser.close()
    # %%
    print("""
    Para o CEP: {}
    Endereço: {}
    Bairro: {}
    Localidade: {}""".format(cep, logradouro, bairro, localidade))
    # %%


#%%

