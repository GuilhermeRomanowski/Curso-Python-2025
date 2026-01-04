'''
Solicite ao usuário o nome de uma fruta e exiba o preço correspondente:
'''

frutas = {"Pera":"R$ 1,25",
          "Goiaba":"R$ 2,15",
          "Abacaxi":"R$ 3,20",
          "Jaca":"R$ 5,80",
          "Laranja":"R$ 0,65",
          "Limão":"R$1,25",
          "Maçã":"R$ 1,50",
          "Banana":"R$ 2,75",
          "Uva":"R$ 1,90"           
          }


fruta = input("""Olá, tudo bem? Segue as frutas que temos disponíveis: 
1) Pera
2) Goiaba
3) Abacaxi
4) Jaca
5) Laranja
6) Limão
7) Maçã
8) Banana
9) Uva
              
Digite o nome da fruta que deseja verificar o preço: """)

if fruta in frutas:
    print(f"A fruta escolhida foi {fruta}. Seu valor custa: {frutas[fruta]}.")

else:
    print("Entre com a fruta correta!")



