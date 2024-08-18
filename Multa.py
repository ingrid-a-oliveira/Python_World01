velocidade = float(input("Digite a velocidade atual do veículo: "))
if velocidade > 80:
    multa = (velocidade-80)*7
    print("Você está acima do limite de velocidade, dirigindo a {} km/h. A multa será de {}.".format(velocidade, multa))
# elif velocidade < 20:
    # print("Você está muito abaixo do limite de velocidade, tome cuidado.")
# else:
    # print("Tenha um bom dia! Dirija com cuidado!")
print("Tenha um bom dia! Dirija com cuidado!")