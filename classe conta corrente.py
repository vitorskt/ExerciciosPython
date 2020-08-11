class Conta_corrente:
    def __init__(self,numero_da_conta,nome,saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self,novo_nome):
        self.nome = novo_nome
        print(f'Nome alterado para {novo_nome}')

    def deposito(self,quantia):
        if quantia < 0:
            print('Quantia inválida')
        else:
            self.saldo += quantia
            print(f'Novo saldo: {self.saldo:.2f}R$')

    def saque(self,quantia):
        if quantia > self.saldo:
            print('Saldo insuficiente')
        elif self.saldo <= 0:
            print('Saldo insuficiente')
        else:
            self.saldo -= quantia
            print(f'Saque efetuado com sucesso. Saldo atual: {self.saldo:.2f}R$')

p1 = Conta_corrente(2743,'Vitor')

print(p1.saldo)
print(p1.numero_da_conta)
p1.deposito(1000)
p1.saque(500)

