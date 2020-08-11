#Faça um programa que peça dois números, base e expoente, calcule e
#mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.

base = int(input('digite a base'))
expoente = int(input('Digite o expoente'))
potencia = 1

for i in range(expoente):
    potencia = potencia*base
print(potencia)
