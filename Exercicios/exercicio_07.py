'''
Utilizando uma função, faça um programa que receba um número.
Verifique se ele é par ou ímpar e exiba o resultado na tela
'''

def par_impar(numero:int):
    if numero % 2 == 0:
        print("É par!")
    else:
        print("É ímpar!")

numero = input("Entre com um número: ")
numero = int(numero)

par_impar(numero)