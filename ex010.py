# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input('Quanto você tem na carteira? R$ '))
print('Convertendo esse valor para dólar você consegue comprar US$ {:.2f}'.format(n1 / 3.27))
