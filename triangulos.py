print('== Triangulos ==')

lado1 = float(input('Digite o primeiro valor'))
lado2 = float(input('Digite o segundo valor'))
lado3 = float(input('Digite o terceiro valor'))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1: #testando se é triângulo

    if lado1 == lado2 == lado3:#testando se é equilátero
        print('O triângulo é Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:#testando se é Isosceles
        print('O triângulo é Isosceles')
    else:
        print('O triângulo é Escaleno')
    
else:
    print('Os valores inseridos não formam um triângulo')
