from time import sleep

lanche = ('suco', 'batata', 'biscoito', 'pudim')#tupla

for cont in range(0, len(lanche)): #conta do item 0 até o 'len' de lanche, ou seja, 4.
    print(lanche[cont])#se printar só o cont, mostrará somente os números de 1 á 4.
    sleep(0.5)
