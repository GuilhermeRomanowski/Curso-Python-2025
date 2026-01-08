#Loteria da babilônia:
#Construa um programa que sorteie um número entre 1 e 15.
#O usuário terá 3 chances de acertar o valor.
#A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
#Caso o usuário acerte, dê os parabéns!!

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número: "))
        except ValueError as err:
            print("Valor inválido. O valor deve ser entre 1 e 15")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario
        print("Valor inválido. O valor deve ser entre 1 e 15")

def check_numbers(numero_sorteio,numero_usuario):

    if numero_usuario == numero_sorteio:
        print("Parabéns!!! Você acertou o número!")
        return True
    
    elif numero_usuario > numero_sorteio:
        print("Número muito alto, tente um número menor.")
        return False
    
    else: 
        print("Número muito baixo, tente um número menor.")  
        return False  

numero_sorteio = random.randint(1,15)
for i in range(3):

    numero_usuario = get_input()
    if check_numbers(numero_sorteio=numero_sorteio,numero_usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!")