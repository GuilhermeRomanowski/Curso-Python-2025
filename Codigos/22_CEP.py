#%%
# request é a biblioteca para consumir dados de API
import requests

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863", 
    "19060100",
    "58038200",
]

url = "https://viacep.com.br/ws/{ceps}/json/"
dados = []

for i in ceps:
    resposta = requests.get(url.format(ceps=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

#.get é o mesmo que jogar o link no navegador. Ele requisita o que tem dentro da URL.
#Alguns tipos abaixo de retorno dos dados.
#resposta #-> resposta 200 = ok
#resposta.raw
#resposta.text
#resposta.json()

# %%
