num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo número: "))
num_03 = int(input("Digite o terceiro número: "))
lista_numeros = [num_01, num_02, num_03]
lista_numeros.sort()
print("O maior número é {}.".format(lista_numeros[2]))
print("O menor número é {}.".format(lista_numeros[0]))