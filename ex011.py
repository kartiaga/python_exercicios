# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura de parede? '))

parede = largura * altura

litroDeTinta = 2

print('A área dessa parede é de {}m²'.format(parede))
print('Para essa parede são necessárias {}l de tinta'.format(parede / litroDeTinta))
