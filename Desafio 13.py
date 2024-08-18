des = 1500.00
proj = 3160.00
coord = 5000.00
ger = 15000.00
carg = input("Digite o cargo que gostaria de consultar o reajuste: ")
if carg == "desenhista":
    print("O salário atual é R${}, mas tivemos o reajuste de 15%, sendo somado ao salário o valor de R${}. Logo, o salário com reajuste é de R${}.".format(des,(des*15/100),(des+(des*15/100))))
if carg == "projetista":
    print("O salário atual é R${}, mas tivemos o reajuste de 15%, sendo somado ao salário o valor de R${}. Logo, o salário com reajuste é de R${}.".format(proj,(proj*15/100),(proj+(proj*15/100))))
if carg == "coordenador":
    print ("O salário atual é R${}, mas tivemos o reajuste de 15%, sendo somado ao salário o valor de R${}. Logo, o salário com reajuste é de R${}.".format(coord,(coord*15/100),(coord+(coord*15/100))))
if carg == "gerente":
    print ("O salário atual é R${}, mas tivemos o reajuste de 15%, sendo somado ao salário o valor de R${}. Logo, o salário com o reajuste é de R${}.".format(ger,(ger*15/100),(ger+(ger*15/100))))