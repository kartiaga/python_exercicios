# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse ângulo

import math
angulo = float(input("Digite o ângulo que você deseja: "))
print("O ângulo de {:.1f} tem o SENO de {:.2f}".format(angulo, math.sin(math.radians(angulo))))
print("O ângulo de {:.1f} tem o COSSENO de {:.2f}".format(angulo, math.cos(math.radians(angulo))))
print("O ângulo de {:.1f} tem a TANGENTE de {:.2f}".format(angulo, math.tan(math.radians(angulo))))