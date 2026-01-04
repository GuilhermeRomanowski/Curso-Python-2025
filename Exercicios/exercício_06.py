'''
Escreva um programa que solicite ao usuário frases. Para parar de solicitar, ele pode apenas apertar "enter".
Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
'''

dic_frase = {}
while True:
    frase = input("Escreva uma frase: ")
    if frase == "":
         break
    
    if frase not in dic_frase:
         dic_frase[frase] = 1
    else:
         dic_frase[frase] += 1

print(f"Você digitou as frases: {dic_frase}")

