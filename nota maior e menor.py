nota1 = float(input('digite sua primeira nota'))
nota2 = float(input('digite sua segunda nota'))
nota3 = float(input('digite sua ultima nota'))
maior = nota1 #achando a maior nota

if nota2 > maior:
    maior = nota2
    
if nota3 > maior:
    maior = nota3
print(f' A sua maior nota foi {maior}')

menor = nota1 #achando a menor nota

if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3
print(f' A sua menor nota foi {menor}')
