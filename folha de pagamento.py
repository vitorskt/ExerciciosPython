print('== Folha de Pagamento ==')
horas = float(input('Quantas horas trabalha por dia?'))
hora_mes = float(input('Quantas horas trabalha ao mês?'))
salario_bruto = horas * hora_mes  # calculo do salario bruto

if salario_bruto <= 900:  # condições para o desconto
    desconto = 0
elif salario_bruto <= 1500:
    desconto = 5
elif salario_bruto <= 2500:
    desconto = 10
else:
    desconto = 20
desconto /= 100.0  # cálculo da folha de pagamento
IR = desconto * salario_bruto
fgts = 11 / 100.0
fgts *= salario_bruto
inss = 10 / 100.0
inss *= salario_bruto
total_descontos = inss + desconto
salario_liquido = salario_bruto - total_descontos

print(f'Seu salário bruto corresponde a : R${salario_bruto}')
print(f'(-) IR (5%) : R${desconto}')
print(f'(-) INSS (10%) : R${inss:.2f}')
print(f'FGTS (11%) : R${fgts}')
print(f'Total de descontos: R${total_descontos}')
print(f'Salário líquido: R${salario_liquido}')
