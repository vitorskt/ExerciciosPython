lista = [12, -2, 4, 8,  29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
resultado = []
negativo = [-2, -17, -52]
print(f'O maior número é {max(lista)}')
print(f'O menor número é {min(lista)}')

for num in lista:
    if num % 2 == 0:
        resultado.append(num)
print(resultado)
print(f'O primeiro item da lista se repete {lista.count(12)} vezes')
media = 0
for num in lista:
    media += num
    media = media / 15
print(f' A média dos elementos é {media:.2f}')
negacao = 0
for num in negativo:
    negacao += num
print(f'A soma dos valores negativos é {negacao}')
