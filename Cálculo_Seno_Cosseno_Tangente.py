import math
ang = (float(input("Digite um ângulo: ")))
esc = input("Escolha entre seno, cosseno e tangente para converter o ângulo: ")
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
if esc == "seno":
    print("O valor de seno é {:.2f}.".format(seno))
elif esc == "cosseno":
    print("O valor de cosseno é {:.2F}.".format(cosseno))
elif esc == "tangente":
    print("O valor da tangente é {:.2f}.".format_map(tangente))
else:
    print("O valor de seno é {:.2f}.".format(seno))
    print("O valor de cosseno é {:.2f}.".format(cosseno))
    print("O valor da tangente é {:.2f}.".format(tangente))