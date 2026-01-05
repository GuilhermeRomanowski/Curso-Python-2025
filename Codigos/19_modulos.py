#%%
#Como aprendemos anteriormente, podemos criar funções. Exemplo de Raíz quadrada:
def sqrt(numero):
    return numero ** (1/2)

#%%
#Porém python existe bibliotecas com funções pré definidas para utilizarmos, sem precisar que criemos funções para raíz quadrada em todo script.
#Para utilizar uma biblioteca, devemos usar o "import" seguido pelo nome da biblioteca desejável.
import math

math.sqrt(9)
math.pow(2,4)
math.e
math.pi

#%%
# A maneira acima importa a biblioteca toda para o python, podemos deixar o script mais leve, importando apenas os módulos que iremos utilizar no código.
# Caso formos utilizar apenas o "pi" e o "e" da bibliteca math, poderemos trazer essas funções com a seguinte linha:
from math import pi, e

math.pi
math.e

#%%
#Podemos também dar um apelido para biblioteca pra utilizar no código ao invés de utilizar o nome completo da biblioteca:
import math as mh

mh.sqrt(25)
mh.pow(8,16)
mh.e
mh.pi