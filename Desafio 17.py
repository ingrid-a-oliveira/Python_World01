from math import hypot

catadj = float(input("Digite o valor do cateto adjascente: "))
catop = float(input("Digite o valor do cateto oposto: "))
# hipot = math.sqrt((catadj**2)+(catop**2))
hip = hypot(catadj, catop)
print("O valor da hipotenusa é {:.2f}.".format(hip))