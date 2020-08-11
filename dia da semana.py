print('== Dia da Semana ==')
dia = int(input('Digite um número entre 1 e 7'))
while dia > 7 or dia < 1:
    print('Número inválido.')
    dia = int(input('Digite um número entre 1 e 7'))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
