print('==== PESO IDEAL ===')
sexo = int(input('Qual é o seu sexo?(1)Masculino (2)Feminino'))
altura = float(input('Digite sua altura'))

if sexo == 2:
    print(f'O seu peso ideal é {(62.1*altura) - 44.7:.2f}KG')
elif sexo == 1:
    print(f'O seu peso ideal é {(72.7*altura) - 58:.2f}KG')
else:
    print('Sexo inválido')
    exit()
