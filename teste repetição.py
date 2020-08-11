login = input('digite seu login')
senha = input('digite sua senha')

while login == senha:
    print('ERROR. O login não pode ser igual a senha')
    login = input('digite seu login')
    senha = input('digite sua senha')
