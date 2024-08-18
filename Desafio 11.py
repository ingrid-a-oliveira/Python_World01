L = float(input("Digite o comprimento que deseja pintar: "))
H = float(input("Digite a altura da parede que deseja pintar: "))
A = L * H
tinta = A*0.5
print("Sua parede tem a dimensão de {}m por {}m, sendo a área {:.2f}m². \nLogo, você precisará de {:.2f}L de tinta para pintar sua parede.".format(L,H,A,tinta))