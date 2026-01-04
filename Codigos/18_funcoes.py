
#%%
#Função matemática
def f(x):
    resultado =  1 + x
    return resultado

f(10)

# %%
#Calculando juros compostos, utilizanod mais de uma variável na função.
def juros_compostos(aporte:int,taxa:float,anos:int)->float:
    """Juros_compostos serve para calcular o retorno financeiro de um aporte.
    Deve-se considerar o valor, taxa de juros atual e tempo (em anos) para o cálculo.

    aporte:
        Um número inteiro que represente o valor em R$.
    
    taxa:
        Um número float entre 0 e 1 que representa o valor ta taxa de juros.
    
    anos:
        Um número inteiro com a quantidade de anos que representa o tempo de investimento.
    """
    return aporte * (1 + taxa)**anos

juros_compostos(1000,0.13,4) #Podemos chamar informando a ordem exata de cada variável.
juros_compostos(aporte=1000,anos=4,taxa=0.13) #Também funciona mesmo invertido, porque foi definido o valor exato de cada variável.
# %%
# Função Ola_mundo

def ola_mundo():
    print("Boas vindas! Olá para você!")
    
ola_mundo()

#%%
#É possível utilizar uma função dentro de outra. Segue exemplo abaixo:

#Função de soma:
def soma(a:float,b:float)->float:
    return a + b

#Função de média -> utilizando a função de SOMA criada acima.
def media(a:float,b:float)->float:
    return soma(a,b)/2

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("Média: ",media(a,b))

# %%
#Podemos ajustar a função de média para trazer mais argumentos.
#Função de soma:
def soma(valores:list)->float:
    return sum(valores)

#Função de média -> utilizando a função de SOMA criada acima.
def media(valores:list)->float:
    return soma(valores)/ len(valores)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

print("Média: ",media([a,b,c]))
# %%
#soma de listas:
a = [1,2,3]
b = [4,5,6]
a+b
# %%
#Podemos ajustar também o código do cálculo da média dessa maneira, assim se aumentar a quantidade de elementos pra calculo da média, a alteração do código é menor que nos modelos acima:
#Função de soma:
#*args é utilizado em lista
def soma(a:float,b:float, *args)->float:
    valores = [a+b] + list(args)
    return sum(valores)

#Função de média -> utilizando a função de SOMA criada acima.
def media(a:float,b:float, *args)->float:
  
    return soma(a, b, *args)/ (len(args)+2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
print("Média: ",media(a,b,c))
# %%
#Calculo_imposto:
#**kwargs é utilizando em dicionário
def calc_imposto(preco:float,tx_imposto_base:float, **kwargs):
    imposto = preco * tx_imposto_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto

calc_imposto(100, 0.03,municipio=0.01, estadual=0.005, nacional= 0.001)

# %%
