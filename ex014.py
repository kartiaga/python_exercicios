# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em C°: '))
print('A temperatura de {}C° corresponde a {}°F'.format(c, ((9 * c) / 5) + 32))
