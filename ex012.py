# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoNormal = float(input('Preço do produto que terá desconto: R$ '))
print('Novo Preço: R$ {:.2f}'.format(precoNormal - (precoNormal * 0.05)))
