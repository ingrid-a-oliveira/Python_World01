dias = int(input("Quantos dias o carro ficou locado? "))
km = float(input("Qual foi a quilometragem rodada com o veículo durante o período de locação? "))
preco = (dias * 60) + (km * 0.15)
print("O valor a ser pago pelo aluguel do veículo por {} dias e pelo percurso de {}km rodados é de R${:.2f}.".format(dias, km, preco))