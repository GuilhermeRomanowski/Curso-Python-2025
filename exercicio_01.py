'''
1. Faça um programa que dê Bom dia, pergunte o nome da pessoa e responde que é um prazer conhecer ela.
2. Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apetar "enter" para continuar.
3. Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.
4. Faça um programa que insira o dobro de um número recebido pelo usuário
'''

#%%
#01
nome = input("Bom dia, qual é o seu nome? ")
print (f"Olá, {nome} é um prazer te conhecer!")


# %%
#02
p1 = "Era uma vez, a chapeuzinho vermelho. Ela queria muito estudar."
p2 = "Ela não sabia por onde começar, então foi procurar ajuda. Até que conheceu seu amigo leo."
p3 = "Leo ensinou a chapeuzinho vermelho a estudar, mas em troca ficou com seu chapéu."
p4 = "Chapeuzinho vermelho ficou feliz em aprender a estudar, porém teve de sacrificar por isso."

input(p1)
input(p2)
input(p3)
input(p4)

print("FIM!!!")
# %%
#03
numero = input("Digite um número inteiro para calcularmos sua raíz quadrada: ")
numero = int(numero)

raiz = numero ** 1/2 # numero * 0.5
raiz = round(raiz, 4)

print(f"A raíz quadrada do {numero} é igual a: {raiz}")

# %%
#04

numero = input("Entre com um número para encontrar seu dobro: ")
numero = int(numero)

dobro = numero * 2

print("O dobro de ",numero, "é ",dobro)
