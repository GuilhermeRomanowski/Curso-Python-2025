#%%
#Lendo arquivos csv.

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines() #.readlines transforma os dados em uma Lista.

print(lines)

#Podemos percorrer as linhas com loop for.
for linha in lines: 
    print(linha)

#Podemos pegar os dados linha a linha e transformar em um dicionário utilizando as colunas como chave do nosso dicionário:
dados = dict() 
#Strip retira o "\n" do texto e Split ele utiliza o que está entre aspas como delimitador.
chaves = lines[0].strip("\n").split(";") 

#Aqui percorremos com loop for criando uma lista dentro de cada chave de dicionário.
for c in chaves:
    dados[c] = []

dados #Criado dicionário com as chaves e lista fazias

#Agora precisamos adicionar os dados corretos em cada chave do dicionário:
for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])

dados

#Podemos criar uma lista de idades, adicionando os dados do dicionário de idades como INT e após isso trazer a média de idades:
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
media
# %%
