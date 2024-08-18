frase = str(input("Digite uma frase: ")).strip().lower()
letra_escolhida = str(input("Digite a letra que deseja buscar: "))
print("Na frase: ''{}'', temos o total de {} letras {}. \nEla aparece pela primeira vez na posição {}. \nE pela última vez na posição {}.".format(frase, frase.count(letra_escolhida), letra_escolhida, frase.find(letra_escolhida)+1, frase.rfind(letra_escolhida)+1))