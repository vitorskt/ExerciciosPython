def contagemregressiva(n):
    if n < 0:
        print('número inválido')
        exit()
    elif n == 0:
        print('BOOOM!!')
    else:
        print(n)
        contagemregressiva(n-1)
        
