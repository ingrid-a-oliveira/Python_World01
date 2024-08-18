from time import sleep
num = int(input("Digite um número de 0 a 9999: \n"))
print("Analisando o número {}.".format(num))
sleep(2)
qnum = (len(num))
if qnum == 1:
    print("Unidade = {}".format(num[0]))
elif qnum == 2:
    print("Unidade = {}".format(num[1]))
    print("Dezena = {}".format(num[0]))
elif qnum == 3:
    print("Unidade = {}".format(num[2]))
    print("Dezena = {}".format(num[1]))
    print("Centena = {}".format(num[0]))
elif qnum == 4:
    print("Unidade = {}".format(num[3]))
    print("Dezena = {}".format(num[2]))
    print("Centena = {}".format(num[1]))
    print("Milhar = {}".format(num[0]))
else:
    print("Erro. Este programa lê apenas números de quatro digitos. Tente novamente")