numero = int(input('Digite um número '))
print(f'Tabuada do {numero}')
for num in range(1,11):
        resultado = numero * num
        print(f'{numero} x {num} = {resultado}')
