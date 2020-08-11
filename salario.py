print('== Reajuste Salarial ==')
salario = float(input('Quanto é o seu salário?'))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

print(f'Salário antes do reajuste:R${salario}')
print(f'Percentual de aumento aplicado:{percentual}%')

percentual = percentual/100.0
aumento = percentual*salario
novo_salario = salario + aumento

print(f'Valor do aumento:R${aumento:.2f}')
print(f'Novo salário após o aumento:R${novo_salario}')
