print("-="*15)
print("Analisador de Triângulos")
print("-="*15)

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do ultimo lado do triângulo: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Os comprimentos digitados formam um triângulo! equilátero!")
    if lado1 == lado2 !=lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("Os comprimentos digitados formam um triângulo isósceles!")
    if lado1 != lado2 != lado3:
        print("Os comprimentos digitados formam um triângulo escaleno!")
else:
    print("Os comprimentos digitados não formam um triângulo!")