#%%
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

#%%
browser = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)

browser.implicitly_wait(10) # tenta a cada 10s

link = ('https://pt.wikipedia.org/wiki/Will_Smith')
browser.get(link)
table = browser.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')

# %%
df = pd.read_html('<table>' + table.get_attribute('innerHTML') + '</table)')[0]

# print da tela
with open('print.png', 'wb') as f:
    f.write(browser.find_element(By.XPATH, '/html/body/div[1]').screenshot_as_png)

#%%
browser.close()

df

# %%
df[df['Ano']==2020]

# %%

df.to_csv('Filmes do Will Smith em 2020', sep=';', index=False)
df
# %%
