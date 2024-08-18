vest = 150.00
sap = 280.00
calc = 99.90
esc = input("Escolha o produto que deseja comprar: ")
if esc == "vestido":
    print ("O preço do vestido é R${}, mas com o desconto de 5% podemos fazer por R${:.2f}.".format(vest,(vest-(vest*5/100))))
if esc == "sapato":
    print ("O preço do sapato é R${}, mas com o desconto de 5% podemos fazer por R${:.2f}.".format(sap,(sap-(sap*5/100))))
if esc == "calça":
    print ("O preço da calça é R${}, mas com o desconto de 5% podemos fazer por R${:.2f}.".format(calc,(calc-(calc*5/100))))