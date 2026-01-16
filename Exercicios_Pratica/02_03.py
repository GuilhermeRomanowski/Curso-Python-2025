#Faça um programa para uma sorveteria, onde o usuário possa escolher:
#Tipo de Sorvere: casquinha (R$1,00), cascão(R$2,50), cestinha(4,00)
#Sabor: Morango, Creme, Chocolate
#Cobertura: Caramelo (R$1,50), Morango (R$1,50), Chocolate (R$1,50), Sem cobertura (R$0.00)
#Apresente o valor a ser pago

tipo = input("Entre com o tipo de sorvete: Casquinha / Cascão / Cestinha")
tipo = tipo.lower()

sabor = input("Escolha o seu sabor [Morango / Creme / Chocolate]")
sabor = sabor.lower()

cobertura = input("Escolha a cobertura [Caramelo / Morango / Chocolate / Sem cobertura]")
cobertura = cobertura.lower()

valor = 0

if tipo == "casquinha":
    valor += 1
elif tipo == "cascão":
    valor += 2.5
elif tipo == "cestinha":
    valor += 4

if cobertura in ("caramelo", "morango", "chocolate"):
    valor += 1.5

if cobertura == "sem cobertura":
    txt = f"Seu sorvete {tipo} com sabor de {sabor} ficou no valor de {valor}"
else:
    txt = f"Seu sorvete {tipo} com sabor de {sabor} e adicionaro de cobertura de {cobertura} ficou no valor de {valor: .2f}"

print(txt)
