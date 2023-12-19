# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Qual o nome do aluno? ')
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

print('A média do aluno {} foi {:.1f}'.format(nome, (n1 + n2)/2))
