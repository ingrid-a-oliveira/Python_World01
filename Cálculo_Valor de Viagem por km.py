distancia = float(input("Digite a distância entre a cidade de origem e a cidade de destino em KM: "))
if distancia <= 0:
    print("A distância não pode ser nula ou negativa. Tente novamente!")
elif distancia <= 200:
    valor = distancia*0.5
    print("O valor da viagem será de R${:.2f}. Faça uma boa viagem!".format(valor))
else:
    valor = distancia*0.45
    print("O valor da viagem será de R${:.2f}. Faça uma boa viagem!".format(valor))