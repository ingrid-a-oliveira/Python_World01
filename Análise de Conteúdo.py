# primeironumero = int(input ("Digite o primeiro número"))
# segundonumero = int(input("Digite o segundo número"))
# terceironumero = int(input("Digite o terceiro número"))
# soma = primeironumero + segundonumero + terceironumero
# print ("A soma é:",soma)
# media = (soma/3)
# print ("A média é: {}".format(media))

# n1 = int(input("Digite n1: "))
# n2 = int(input("Digite n2: "))
# sm = n1 + n2
# print ("A soma entre {} e {} é {}".format(n1,n2,sm))

valor = input("Digite algo: ")
print("O conteúdo digitado é alpha? ",valor.isalpha())
print("O conteúdo digitado é numérico? ",valor.isnumeric())
print("O conteúdo digitado só possui letras minúsculas? ",valor.islower())
print("O conteúdo digitado só possui letras maiúsculas? ",valor.isupper())      
print("O valor digitado é alpha numérico? ",valor.isalnum())