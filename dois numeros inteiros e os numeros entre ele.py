num1 = int(input('Digite um número'))
num2 = int(input('Digite outro número'))
cont = 0
while num2 < num1:
    num1 = int(input('Digite um número'))
    num2 = int(input('Digite outro número'))

else:
        for i in range(num1+1,num2):
            print(i)
            cont = cont + i
print(f'A soma dos valores acima é {cont}')

