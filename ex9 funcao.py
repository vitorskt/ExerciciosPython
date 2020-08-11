#Reverso do número. Faça uma função que retorne o reverso
#de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    n = str(n[::-1])
    print(n)
n = str(input('Digite um número: '))
reverso(n)

