# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno_1 = str(input("Diga o nome do primeiro aluno: "))
aluno_2 = str(input("Diga o nome do segundo aluno: "))
aluno_3 = str(input("Diga o nome do terceiro aluno: "))
aluno_4 = str(input("Diga o nome do quarto aluno: "))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

random.shuffle(lista)
print("A ordem de apresentacao será: ")
print(lista)
