salario = float(input("Digite o salário do funcionário que deseja calcular o aumento: "))
aumento_porcentual = int(input("Digite a porcentagem que o funcionário receberá de aumento: "))
# if salario > 1250:
    # salario_aumento = salario*1.1
    # print("O salário do funcionário é de R${:.2f} e com aumento passará a ser R${:.2f}.".format(salario, salario_aumento))
# else:
    # salario_aumento = salario*1.15
    # print("O salário do funcionário é de R${:.2f} e com aumento passará a ser R${:.2f}.".format(salario, salario_aumento))
salario_aumento = salario + (salario*(aumento_porcentual/100))
print("O salário do funcionário é de R${:.2f} e ele receberá {}% de aumento. O salário passará a ser de R${:.2f}.".format(salario, aumento_porcentual, salario_aumento))