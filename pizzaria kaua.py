print("PIZZARIA COMA BASTANTE - SEJA BEM VINDO")
print("___ CARDÁPIO DE PREÇOS____")
print("  ")
print("**PIZZAS - SABORES***")
print("CALABRESA, FRANGO, CATUPIRY")
print("**PIZZAS - TAMANHO***")
print(" PIZZA PEQUENA R$ 10,00  ")
print(" PIZZA MÉDIA  R$ 15,00  ")
print(" PIZZA GRANDE R$ 20,00  ")
print("**REFRIGERANTES*****")
print(" COCA-COLA R$ 7,00  ")
print(" GUARANÁ R$ 6,00  ")
print(" FANTA R$ 5,00   ")
print("____________")
print(" ") 
print("FAÇA SEU PEDIDO PARA A PIZZA:")
print("1 - CALABRESA")
print("2 - FRANGO")
print("3 - CATUPIRY")
print("____________")

# lê a escolha do sabor da pizza do usuário e converte pra inteiro.
pedidopizza = int(input())

print("DIGITE O TAMANHO DA PIZZA:")
print("P - PEQUENA")
print("M - MÉDIA")
print("G - GRANDE")
print("____________")

# lê a escolha do tamanho da pizza do usuário e converte para maiúsculo 
tampizza = input().upper()

print("FAÇA O SEU PEDIDO PARA REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
print("____________")

# lê a escolha do refrigerante do usuário e converte para inteiro.
pedidorefri = int(input())

# calcule o preço total e descreve o pedido utilizando elif com parênteses 
if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABRESA, PEQUENA, COCA-COLA"

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.0 + 6.00 
    pedidos = "CALABRESA, PEQUENA, GUARANÁ"

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.0 + 5.00 
    pedidos = "CALABRESA, PEQUENA, FANTA"


elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.0 + 6.00 
    pedidos = "FRANGO, PEQUENA, GUARANÁ"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.0 + 7.00 
    pedidos = "FRANGO, PEQUENA, COCA-COLA"    

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.0 + 5.00 
    pedidos = "FRANGO, PEQUENA, FANTA"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.0 + 6.00 
    pedidos = "CATUPIRY, PEQUENA, GUARANÁ"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.0 + 7.00 
    pedidos = "CATUPIRY, PEQUENA, COCA-COLA"  

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.0 + 5.00 
    pedidos = "CATUPIRY, PEQUENA, FANTA "

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.0 + 6.00 
    pedidos = "CALABRESA, MÉDIA, GUARANÁ"


elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.0 + 7.00 
    pedidos = "CALABRESA, MÉDIA, COCA-COLA"


elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.0 + 5.00 
    pedidos = "CALABRESA, MÉDIA, FANTA"


elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.0 + 6.00 
    pedidos = "FRANGO, MÉDIA, GUARANÁ"
        

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.0 + 7.00 
    pedidos = "FRANGO, MÉDIA, COCA-COLA"


elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.0 + 5.00 
    pedidos = "FRANGO, MÉDIA, FANTA"


elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.0 + 6.00 
    pedidos = "CATUPIRY, MÉDIA, GUARANÁ"    


elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.0 + 7.00 
    pedidos = "CATUPIRY, MÉDIA, COCA-COLA"     


elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.0 + 5.00 
    pedidos = "CATUPIRY, MÉDIA, FANTA"     


elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.0 + 7.00 
    pedidos = "CALABRESA, GRANDE, COCA-COLA"


elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.0 + 6.00 
    pedidos = "CALABRESA, GRANDE, GUARANÁ"    

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.0 + 5.00 
    pedidos = "CALABRESA, GRANDE, FANTA"   

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.0 + 7.00 
    pedidos = "FRANGO, GRANDE, COCA-COLA"    

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.0 + 6.00 
    pedidos = "FRANGO, GRANDE, GUARANÁ"     

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.0 + 5.00 
    pedidos = "FRANGO, GRANDE, FANTA"   

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.0 + 7.00 
    pedidos = "CATUPIRY, GRANDE, COCA-COLA"    

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.0 + 6.00 
    pedidos = "CATUPIRY, GRANDE, GUARANÁ"    

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.0 + 5.00 
    pedidos = "CATUPIRY, GRANDE, FANTA"     

else:  
    precopagar =  0.0
    pedidos = "PEDIDO INVÁLIDO"

# Exibe o resumo do pedido e o preço total a pagar.
print("____________")
print(f"O TOTAL A PAGAR É: R$ {precopagar:.2f}")
print("____________")
print(f"OS PEDIDOS FORAM {pedidos}")
print("____________")
print("BOM APETITE SEJA BEM VINDO")