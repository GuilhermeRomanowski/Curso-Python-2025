#Altere o programa anterior para que considere a quantidade de garrafas.

tipo = input("Escolha um tipo de água: 1) Água mineral natural / 2) Água mineral com gás")
qtd = input("Qual a quantidade de garrafas? ")


if tipo == "1":
    valor = 1.5 * qtd
    print(f"Valor Total: {valor}")
elif tipo == "2":
    valor = 2.5 * qtd
    print(f"Valor Total: {valor}")
else:
    print("Entre com o dados válidos")

