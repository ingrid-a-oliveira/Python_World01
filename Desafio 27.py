nome = str(input("Digite seu nome completo: ")).strip().title().split()
print("Seu primeiro nome é {}. \nSeu último nome é {}.".format(nome[0], nome[-1]))
