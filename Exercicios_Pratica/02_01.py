#Faça um programa que venda uma garrafa de água:
#Se o cliente escolher água mineral, será cobrado R$1,50
#Se o cliente escolher água com gás, será cobrado R$2,50

tipo = input("Escolha um tipo de água: 1) Água mineral natural / 2) Água mineral com gás")

if tipo == "1":
    print("Valor: R$1,50")
elif tipo == "2":
    print("Valor: R$2,50")
else:
    print("Entre com um valor válido!")