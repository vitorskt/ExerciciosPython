resultado = 0
for soma in range(1,501,2):
    if soma % 3 == 0:
        resultado = resultado+soma
print(f'A soma de todos os valores solicitados é {resultado}')
