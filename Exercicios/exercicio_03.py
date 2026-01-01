'''
1 - Faça um programa que conte quantas vezes a leta "a" aparece em uma palavra.
2 - Faça um programa que receba  4 alturas usando laço de repetição e realize a soma dessas alturas.
3 - Faça um programa  que receba uma quantidade indefinida de valores correspondentes a "saldo em conta",
mas quando o usuário apertar "enter" sem digitar valor algum, o programa para de receber valores e exibe
a soma de todos valores digitados anteriormente.
'''

#%% 1 - Contagem de A na palavra
palavra = input("""Digite uma palavra com todos caracteres minúsculos para contarmos quantas letras "a" tem nela""")
quantidade = 0
for i in palavra:
    if i == "a":
        quantidade += 1
    
print("A palavra digitada contém a leta 'a'", quantidade, "vezes.")
#%% 2 - Alturas
soma = 0
entrada = 4

while entrada > 0:
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura
    entrada -= 1

print("A soma das alturas é:", soma)

#%%2 - Alturas utilizando "for"
soma = 0
entrada = 4

for i in range(entrada):
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("A soma das alturas é:", soma)


#%% 3 -Saldo em Conta - Feito sozinho
saldo_total = 0
count = 0
while count == 0:
    saldo = input("Entre com o saldo: ")
    if saldo == "":
        count += 1
    else:
        saldo_total += float(saldo)
    
print(saldo_total)


# %% 3 - Saldo em Conta feito com Professor:
saldo_total = 0

while True:
    saldo = input("Entre com o saldo: ")
    if saldo == "":
        break
    
    saldo_total += float(saldo)
    
print(saldo_total)

# %%
