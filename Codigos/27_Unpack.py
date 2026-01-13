#%%
A = 1
B = 5
print(A)
print(B)

#Jogo valor de A em C, de B em A e o antigo de A que estava em C em B. Assim trocamos os valores da variável.
C = A
A = B
B = C
print(A)
print(B)

#Também podemos trocar os valores entre as variáveis da seguinte maneira:
A, B = B, A
print(A)
print(B)

#%%
#Podemos atribuir valores a 2 ou mais variáveis separando-os por ","
a, b, c, d = 1, 2, 3, 4
print(a,b,c,d)
#Não faz sentido sempre que tivermos valores novos a serem incluídos na variável, utilizamos *
a, b, *resto = 1,2,3,5,7,6
print(a,b,resto)

# %%
#Podemos utilizar o mesmo conceito em uma função, normalmente não chamamos a variável de resto e sim de "args".
def soma(a,*args):
    total = a + sum(args)
    return total
soma(1,3,5,4,1,1,1,2,3)
# %%
#também funciona da seguinte maneira
def soma_quatro(a,b,c,d):
    return a+b+c+d
values = [1,2,3,4]
soma_quatro(*values)

#Também funciona com a função padrão de soma:
soma(*values)

# %%
