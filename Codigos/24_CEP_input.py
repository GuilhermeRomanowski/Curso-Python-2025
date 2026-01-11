#%%
import requests
import json 

ceps = input("Entre com o CEP: ")

url = "https://viacep.com.br/ws/{ceps}/json/"

resposta = requests.get(url.format(ceps=ceps))
if resposta.status_code == 200:
    print(resposta.json())



# %%
