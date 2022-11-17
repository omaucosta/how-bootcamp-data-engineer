#%%
from cgi import test
import requests
import json

#%%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

ret = requests.get(url)
# %%
# Verificando se tem resposta do endpoint
if ret:
    print(ret)
else:
    print("Falhou")

# %%
dolar = json.loads(ret.text)['USDBRL'] # formando o json, a partir do 'USDBRL'

# %%
print (f"20$ hoje custam {float(dolar['bid']) * 20} reais")
# %%

def cotacao (valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')] # formando o json, a partir do 'USDBRL'
    print (f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

# %%
cotacao (20,'USD-BRL')
# %%
# tratando erros:

def multi_moeda(valor, moeda):
    # last_money = ['USD-BRL','EUR-BRL','BTC-BRL', 'RPL-BRL', 'JPY-BRL']
    
    # for moeda in last_money:
    #     try:
            url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
            ret = requests.get(url)
            dolar = json.loads(ret.text)[moeda.replace('-','')] # formando o json, a partir do 'USDBRL'
            print (f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
        # except:

#%%
import backoff
import random

@backoff.on_exception(backoff.expo, ConnectionAbortedError, ConnectionRefusedError, TimeoutError, max_time=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexao foi finalizada')
    if rnd < .4:
        raise ConnectionRefusedError('Conexao foi recusada')
    if rnd < .6:
        raise TimeoutError('O tempo de espera foi excedido')
    else:
        return 'Ok!'

# %%
test_func()

#%%
import logging

#%%

log = logging.getLogger()