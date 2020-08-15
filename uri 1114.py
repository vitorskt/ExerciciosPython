correto = 2002
senha = int(input())

while senha != correto:
    print("Senha Invalida")
    senha = int(input())
else:
    print("Acesso permitido")
