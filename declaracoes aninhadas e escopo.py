x = 25

def local(): # X aqui é Local
    x = 50
    return x

#podemos usar a função locals() para retornar um dicionario com as variaveis locais

def local():
    a = 100
    print(locals())
local()
