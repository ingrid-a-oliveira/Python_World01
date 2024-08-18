m = float(input("Digite o valor em metros que deseja converter: "))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000
convert = input("Digite o tipo de medida que deseja: ")
if convert == "dm":
    print(dm)
elif convert == "cm":
    print(cm)
elif convert == "mm":
    print (mm)
elif convert == "dam":
    print (dam)
elif convert == "hm":
    print (hm)
elif convert == "km":
    print (km)
