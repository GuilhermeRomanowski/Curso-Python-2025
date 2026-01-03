# %%

#Uma maneira de definir listas:
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)

# %%
#A lista pode ser de qualquer tipo. Exemplo:

cliente = ["Guilherme","Barbosa",31,1.81,True,"casado"]
print(cliente)

#Descobrindo tipo de variável
type(cliente)

#Acessando posições dentro da lista:
#idade
print(cliente[2])
#altura
print(cliente[3])


#%%

idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

#SOMA
print("Soma das idades: ",sum(idades))

#MÉDIA
print("Média das idades: ",sum(idades)/ len(idades))

#MENOR IDADE
print("Menor das idades: ",min(idades))

#MAIOR IDADE
print("Maior das idades: ",max(idades))

# %%
#É possível colocar listas dentro de listas, ela contabiliza 1 elemento do tipo "LISTA"
teo = ["Teo Calvo",
       32, 
       True,
       "Casado",
       ["estagiário","ds jr.","ds pl","ds sr.","head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana","Maria","Claudia"]]

print("Tamanho de teo: ",len(teo))

#1º maneira de acessar dados de uma lista dentro da lista: LISTA[elemento da lista][elemento da lista informada no colchete anterior].
teo[6][0]
#2º maneira
exs = teo[6]
primeira_ex = exs[0]

print(primeira_ex)

#Como pegar o último elemento da lista dentro da lista :
tamanho = len(teo)
pos = tamanho - 1
teo[pos][0]

teo[pos][len(exs)-1]

#último elemento da lista [-1]. 
#Todo trabalho acima, se resumiria ao seguinte comando:
teo[-1][-1]

#Fatiamento utilizar ":" entre o intervalo do índice da lista para trazer todos elementos
#Lembra  maneira do range do excel para buscar uma coluna: (A1:A10 no excel pega a coluna da linha 1 até a 10)
#No python segue a maneira que fica para buscar do elemento 1 até o elemento 5:
print(teo[0:4])

#O primeiro parâmetro do índice é sempre 0. Ou seja se a lista tem 8 elementos, o índice dela é contabilizado de 1 a 7



#Buscando elementos da lista dentro da lista:
teo[4][3:5]

teo[4][-2:] # Ele contabiliza -2 do último elemento e puxa até o final da lista.
#Não é preciso colocar o valor do último elemento caso queira puxar até o final.
#teo[start : stop], onde o start é o primeiro elemento e stop é o segundo elemento.

#Como percorrer a lista de salário que está dentro da lista teo de trás pra frente:
salarios = teo[5]
salarios[::-1]
#Acima ele navega da seguinte maneira: salarios[start:stop:step]
#start, onde começa. Stop onde termina. Step, como vou percorrer (-1 ele percorre de trás pra frente).
#Step -1 é de trás pra frente
#Step 2 é de 2 em 2 elementos.
#Por padrão o Step é sempre 1.
# %%
