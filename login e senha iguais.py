login = input('digite seu login: ').lower()
senha = input('digite sua senha: ').lower()

while senha == login:
    print('A senha não pode ser igual ao login!!')
    login = input('digite seu login: ').lower()
    senha = input('digite sua senha: ').lower()
print('Cadastro efetuado com sucesso!!')
