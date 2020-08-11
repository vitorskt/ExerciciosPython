mult = 1
soma = 0
for num in range(5):
    res = int(input('Digite um numero'))
    soma += res
    mult *= res
print(f'A soma dos números é {soma}')
print(f'A multiplicação dos números é {mult}')
