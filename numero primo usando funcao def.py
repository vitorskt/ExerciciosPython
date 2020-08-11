def primo(num):
#método pra checar se o número é primo
    if num == 1:
        print('Não é primo')
    else:
        for n in range(2,num):
            if num % n == 0:
                print('Não é primo')
                break
        else:
            print('É primo!')
