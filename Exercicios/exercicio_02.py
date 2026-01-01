'''
1. Faça um programa que venda uma garrafa de água:
    a)Se o cliente escolher água mineral natural, será cobrado R$ 1.50.
    b)Se o cliente escolher água mineral com gás, será cobrado R$ 2.50.
2. Altere o programa anterior para considerar a quantidade de água.
3.Faça um programa de uma sorveteria, onde o usuário pode escolher:
    a)Tipo de sorvete: Casquinha(R$1.00), cascão(R$2.50), cestinha(R$4.00).
    b)Sabor do sorvete: Morango, Creme, Chocolate.
    c)Cobertura: Caramelo(R$1.50), Morango(R$1.50), Chocolate(R$1.50), sem cobertura(R$0.00)
'''

#%% 01 e 02 - Garrafa de água
nome = input("Olá, qual o seu nome? ")
print(f"Olá, {nome} é uma satisfação conhecer você.")
perg = input("Deseja compara uma água? (Sim/Não) ")
if perg == "Sim":
    agua = input("""Digite a opção de qual água você deseja comprar:
    (1) Água natural (R$1.50)
    (2) Água com gás (R$2.50) 
    """)
  
    if agua == "1":
         quantidade = input("Digite a quantidade de águas naturais você deseja: ")
         quantidade = int(quantidade)
         valor = quantidade * 1.50
         print(f"O valor da água é R${valor}, pode pagar no caixa!")
    elif agua == "2":
        quantidade = input("Digite a quantidade de águas naturais você deseja: ")
        quantidade = int(quantidade)
        valor = quantidade * 2.50
        print(f"O valor da água é R${valor}, pode pagar no caixa!")

    else:
         print("Você digitou a opção errada. O atendimento será encerrado!")
elif perg == "Não":
     print(f"Tudo bem {nome}, se mudar de ideia é só retornar. Temos água natural e com gás. Tenha um ótimo dia!")
else:
     print("Você digitou a opção errada. O atendimento será encerrado!")



# %%03 - Sorveteria 
tipo = input("""Olá, bem vindo ao atendimento virtual da sorveteria maluca!
             Digite a opção de qual tipo de sorvete você deseja:
             (1) Casquinha R$1.00
             (2) Cascão R$2.50
             (3) Cestinha R$4.00

             """)
conta = 0
if tipo == "1":
     conta = 1.00
            
elif tipo == "2":
    conta = 2.50

elif tipo == "3":
    conta = 4.00

if conta != 0:
    sabor = input("""Muito obrigado pela escolha. Qual sabor de sorvete você deseja?
                   (1) Morango
                   (2) Creme
                   (3) Chocolate""")
    if sabor == "1":
       cobertura = input("""Você escolheu Morgango Digite qual sabor de cobertura deseja:
              (1) Caramelo R$1.50
              (2) Morango R$1.50
              (3) Chocolate R$1.50
              (4) Sem Cobertura R$0.00
              """)
       if cobertura == "1":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "2":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "3":   
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "4":
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       else:
          print("Opção inválida, tente novamente mais tarde e digite a opção correta!!!")     
    elif sabor == "2":
       cobertura = input("""Você escolheu Creme Digite qual sabor de cobertura deseja:
              (1) Caramelo R$1.50
              (2) Morango R$1.50
              (3) Chocolate R$1.50
              (4) Sem Cobertura R$0.00
              """)
       if cobertura == "1":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "2":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "3":   
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "4":
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       else:
          print("Opção inválida, tente novamente mais tarde e digite a opção correta!!!")     

    elif sabor == "3":
       cobertura = input("""Você escolheu Chocolate Digite qual sabor de cobertura deseja:
              (1) Caramelo R$1.50
              (2) Morango R$1.50
              (3) Chocolate R$1.50
              (4) Sem Cobertura R$0.00
              """)
       if cobertura == "1":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "2":
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "3":   
           conta = conta + 1.50
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       elif cobertura == "4":
           print(f"Muito obrigado pela escolha. Estamos preparando O valor do seu sorvete. Faça o pagamento no valor de {conta} e retire o produto em seguida!")
       else:
          print("Opção inválida, tente novamente mais tarde e digite a opção correta!!!")     

    else:
        print("Opção inválida, tente novamente mais tarde e digite a opção correta!!!")       
else:
    print("Opção inválida, tente novamente mais tarde e digite a opção correta!!!")


# %%
