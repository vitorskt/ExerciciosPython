numero = []
par = []
impar = []

for i in range(5):
    digito = int(input("Digite um número: ")) 
    numero.append ( digito )
    if (digito % 2) == 0:
         par.append (digito)
    else:
        impar.append (digito)
numero.sort()
print (f'O conjunto dos caracteres são: {numero}')
print (f'Os caracteres Pares são: {par}')
print (f'Os caracteres Ímpares são: {impar}')
