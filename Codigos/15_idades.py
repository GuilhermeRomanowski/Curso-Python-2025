
# %%
idades = [17, 32, 56, 87]
print(idades)
#As listas são objetos mutáveis!!!
# É possível adicionar um novo elemento dentro dela
# utilizando append conforme abaixo:

idades.append(32)
print(idades)
# %%
#Criando lista vazia
idades = []

#Fazendo o usuário digitar a idade para criar uma lista com as idades digitadas.
#Caso o usuário não queira mais entrar com a idade, ele simplesmente aperta enter para exibir a lsita com todas as idades digitadas.
while True:
    idade = input("Entre com a idade: ")
    if idade == "":
        break

    idades.append(int(idade)) #Necessário converter pra inteiro, porque o input sempre entra como string.

print(idades)

#Podemos também criar algumas estatísticas das idades digitadas e exibir ao usuário:
media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTD:", qtd)

