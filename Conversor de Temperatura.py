escolha = (input("Você gostaria de converter sua temperatura em graus celsius para fahrenheit ou para kelvin? Digite 1 para fahrenheit ou 2 para kelvin: "))
if escolha == "1":
    celsius = float(input("Digite a temperaruta em graus celsius que deseja converter: "))
    print("A temperatura em Fahrenheit é {}°F.".format(celsius + 273.15))
elif escolha == "2":
    celsius = float(input("Digite a temperaruta em graus celsius que deseja converter: "))
    print("A temperatura em Kelvin é {}°K.".format((celsius * 9/5) + 32))
else:
    print("A opção não está disponível. Por favor, tente novamente.")