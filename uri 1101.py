x = 0
maior = 0
menor = 0

while True:
    valor1, valor2 = map(int, input().split())

    if valor1 <= 0 or valor2 <= 0:
        break

    maior = valor1 if valor1 > valor2 else valor2
    menor = valor2 if valor2 < valor1 else valor1

    if maior > menor:
        x = maior
        maior = menor
        menor = x

    soma = 0

    while maior <= menor:
        print(maior, end=' ')
        soma += maior
        maior += 1
    print('Sum={}'.format(soma))
