# nome = str(input("Digite o seu nome: "))
# if nome == "Ingrid":
    # print("Que nome lindo você tem!")
# else:
    # print("Seu nome é tão normal.")
# print("Bom dia, {}!".format(nome))

n1 = float(input("Digite a nota da n1: "))
n2 = float(input("Digite a nota da n2: "))
media = (n1 + n2) / 2
if media >= 6:
    print("Sua média é {:.2f} e está boa, parabéns!".format(media))
else:
    print("Sua média é {:.2f}. Você precisa recuperar sua nota. Será necessário fazer a PS!".format(media))
    