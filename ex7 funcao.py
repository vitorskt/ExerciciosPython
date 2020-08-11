#Faça um programa que use a função valorPagamento para determinar o valor
#a ser pago por uma prestação de uma conta. O programa deverá solicitar
#ao usuário o valor da prestação e o número de dias em atraso e passar estes
#valores para a função valorPagamento, que calculará o valor a ser pago e
#devolverá este valor ao programa que a chamou. O programa deverá então
#exibir o valor a ser pago na tela. Após a execução o programa deverá voltar
#a pedir outro valor de prestação e assim continuar até que seja informado
#um valor igual a zero para a prestação. Neste momento o programa deverá
#ser encerrado, exibindo o relatório do dia, que conterá a quantidade e
#o valor total de prestações pagas no dia. O cálculo do valor a ser pago
#é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da
#prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por
#dia de atraso.

def valorPagamento(valor_p, dias_a): #se dias atrasado for menor que 1
    if dias_a < 1:
        valor = valor_p
        print(valor)
        return valor
    else: #senão, calcula o valor do pagamento com atraso
        valor = (valor_p + valor_p * 0.03 + 0.01 * dias_a)
        print(valor)
        return valor
 
valor = []
valor_p = 0
dias_a = 0
quant_pagar = 0
valortotal = 0
 
while True:
    quant_pagar += 1
    valor_p = float(input('Qual o valor da prestação? '))
    dias_a = int(input('Quantos dias está em atraso? '))
    if valor_p == 0:
        break
    valor.append(valorPagamento(valor_p, dias_a))
 
quant_pagar -= 1
for i in range(quant_pagar):
    valortotal += valor[i]

print(f'Relatorio do dia: foram pagas {quant_pagar} prestacoes no valor: {valor}')
print(f'Valor total em prestaçoes pagas: {valortotal:.2f}')
