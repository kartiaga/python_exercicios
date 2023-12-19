# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e 
# todas as informações possíveis sobre ele.

n1 = input('Digite algo: ')

print('O tipo primitivo desse é {}'.format(type(n1)))
print(n1.isnumeric())
print(n1.isalpha())
print(n1.isupper())
