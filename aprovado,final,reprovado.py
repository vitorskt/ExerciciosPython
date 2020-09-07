nota1 = float(input('digite sua primeira nota'))
nota2 = float(input('digite sua segunda nota'))
nota3 = float(input('digite sua terceira nota'))
nota4 = float(input('digite sua ultima nota'))
resultado = nota1+nota2+nota3+nota4
resultado = resultado/4
print(f'A sua média anual é igual a {resultado}')
if resultado >= 7.0:
    print('Você está aprovado, parabéns!!!')
elif resultado >= 5.0:
    print('Você está na final, lembre-se de estudar!!')
else:
    print('Você está reprovado!')
