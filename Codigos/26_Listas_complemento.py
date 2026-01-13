#%%
#Podemos utilizar laço "for" para incluir dados em uma lista. Exemplo:

x = []

for i in range(1,101):
    x.append(i)

print(x)

#%%
#Podemos também fazer com o for dentro da lista:

y = [i for i in range (1,101)]
print (y)
# %%
#Para saber se o número é par ou não:
def e_par(x):
    return x % 2 == 0

z = [e_par(i) for i in range (1,101)]
z

#Para incluir somente números pares na lista:
w = [i for i in range (1,101) if e_par(i)]
w
# %%
