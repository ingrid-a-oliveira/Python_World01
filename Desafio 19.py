import random
print("Os cinco alunos com as notas mais baixas no mês farão parte de um sorteio onde o sorteado deverá ser auxiliar dos professores durante as aulas: ")
a1 = input("Digite o nome do aluno com as notas mais baixas: ")
a2 = input("Digite o nome do segundo aluno com as notas mais baixas: ")
a3 = input("Digite o nome do terceiro aluno com as notas mais baixas: ")
a4 = input("Digite o nome do quarto aluno com as notas mais baixas: ")
a5 = input("Digite o nome do quinto aluno com as notas mais baixas: ")

alunos = [a1,a2,a3,a4,a5]

sorteado = random.choice(alunos)
print("O aluno sorteado foi {}.".format(sorteado))