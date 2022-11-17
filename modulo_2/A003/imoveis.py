#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# %%
url = 'https://www.vivareal.com.br/aluguel/espirito-santo/vitoria/apartamento_residencial/?pagina={}'

#%%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)

# %%
soup
# %%
houses = soup.find_all('a',{'class': 'property-card__content-link js-card-title'})
houses
len(houses)

# %%
qtd_houses = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.',''))
qtd_houses

# %%
house = houses[0]

# %%
house

#%%
df = pd.DataFrame(
    columns=[
        'Descrição',
        'Endereço',
        'Área',
        'Quartos',
        'WC',
        'Vagas',
        'Valor',
        'Condomínio',
        'Wlink'
    ]
)

df
i = 0

# %%
# strip () --> remove todos os espaços do string
while qtd_houses > df.shape[0]:
    i += 1
    print(f"valor i: {i} \t\t qtd_houses: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all('a',{'class': 'property-card__content-link js-card-title'})

    for house in houses:
        try: 
            descricao = house.find('span',{'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try: 
            endereco = house.find('span',{'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try: 
            area = house.find('span',{'class': 'property-card__detail-value'}).text.strip()
        except:
            area = None
        try: 
            quartos = house.find('li',{'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try: 
            wc = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            wc = None
        try: 
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = None
        try: 
            valor = house.find('div', {'class': 'property-card__price'}).p.text.strip()
        except:
            valor = None
        try: 
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try: 
            wlink = 'https://vivareal.com.br' + house['href']
        except:
            wlink = None
        df.loc[df.shape[0]] = [
                descricao,
                endereco,
                area,
                quartos,
                wc,
                vagas,
                valor,
                condominio,
                wlink
            ]

#%%
df

#%%

# %%