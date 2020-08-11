class Bola:
    def __init__(self,cor,cir,mat):
        self.cor = cor
        self.cir = cir
        self.mat = mat

    def mostra_cor(self):
        print(self.cor)

    def troca_cor(self,nova_cor):
        
        self.cor = nova_cor
        print('A cor foi alterada')


b1 = Bola('Azul', 15, 'Plastico')

b1.mostra_cor()
b1.troca_cor('Amarelo')
b1.mostra_cor()
