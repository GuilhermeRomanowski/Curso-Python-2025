#Os Dicionários são definidos por {"chave":"valor"}

dados_teo = {"Nome":"teo",
             "Sobrenome":"Calvo",
              "Filhos":True,
              "formação":["estatística","brigada datascience"],
              "cargos":[
                  {"nome":"ds_jr","empresa":"teps"},
                  {"nome":"ds_pl","empresa":"sas"},
                  {"nome":"ds_sr","empresa":"boticario"},
                  {"nome":"ds espec.","empresa":"via varejo"}]
              }

print(dados_teo)

#Podemos chamar o valor do dicionário chamando pela chave dele.
dados_teo["Sobrenome"]

#Podemos trazer uma lista dentro do dicionário chamando pelo valor da chave também.
print(dados_teo["formação"][-1])

#Podemos fazer um dicionário dentro do valor feito por uma lista inteira e gerando novos dicionários dentro dessa lista.
#Para acessar o último elemento desde dicionário feito dentro de cargos utilizamos:
print(dados_teo["cargos"][-1]["empresa"])

#Podemos adicionar elementos no dicionário com o seguinte comando:
dados_teo["estado_civil"] = "casado"

print(dados_teo)

#Podemos descobrir as chaves do dicionário com o seguinte comando:
print("Chaves: ",dados_teo.keys())

#Podemos também exibir os valores das chaves:
print("Valores: ", dados_teo.values())

#Podemos combinar também para trazer os pares (chave/valor):
print("Itens: ", dados_teo.items())

#Podemos utilizar o loop no dicionário:
for i in dados_teo:
    print(i, "->", dados_teo[i])
    #A variárel i acessa as chaves do dicionário, assim podemos colocar o "i" em colchetes para acessar o elemento.

#Podemos utilizar o loop para lista de variáveis no dicionário
for chave, valor in dados_teo.items():
    print(chave, "->", valor)