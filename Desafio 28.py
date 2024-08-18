import random
num = [0, 1, 2, 3, 4, 5]
num_sorteado = random.choice(num)
# num_sorteado = randint (0, 5)
valor_escolhido = int(input("Digite o valor que você acha que o computador escolheu: "))
if valor_escolhido == num_sorteado:
    print("Parabéns, você venceu!")
else:
    print("Não foi dessa vez, o valor sorteado pelo computador foi {}. O computador venceu!".format(num_sorteado))