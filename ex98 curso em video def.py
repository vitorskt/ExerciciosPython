from time import sleep

def contador(i,f,p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!!')
    print('-='*20)

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini,fim,pas)
