# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
aluno_1 = str(input("Diga o nome do primeiro aluno: "))
aluno_2 = str(input("Diga o nome do segundo aluno: "))
aluno_3 = str(input("Diga o nome do terceiro aluno: "))
aluno_4 = str(input("Diga o nome do quarto aluno: "))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = choice(lista)
print("O aluno escolhido foi {} ".format(sorteado))