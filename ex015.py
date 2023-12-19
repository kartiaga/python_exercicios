# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro esteve alugado? '))
kmPercorrido = float(input('Quantidade de quilometros rodados: '))

preco = (dias * 60) + (kmPercorrido * 0.15)

print('O preço a pagar por {}Km rodados e {} dias é R$ {:.2f}'.format(kmPercorrido, dias, preco))