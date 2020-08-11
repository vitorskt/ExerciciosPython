print('== DOAÇÃO DE SANGUE ==')
idade = int(input('Qual é sua idade?'))
if idade >= 16 and idade <= 69:
    peso = float(input('Qual é o seu peso?'))
elif peso < 16:
    print('sua idade não é permitida para a doação')
if peso < 50:
    print('Você está abaixo do peso necessário')
elif peso > 50:
    doença = str(input('esteve gripado, resfriado ou com febre recentemente?'))
        
