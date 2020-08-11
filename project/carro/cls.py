class Carro:
    def __init__(self,direcao, motor):
        self.direcao = direcao
        self.motor = motor
    

    def calcular_velocidade(self):
        return self.motor.velocidade
    

    def acelerar(self):
        self.motor.acelerar()
    

    def frear(self):
        self.motor.frear()
    

    def calcular_direcao(self):
        return self.direcao.valor
    

    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}


    def __init__(self):
        self.valor = NORTE

    
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]




class Motor:
    def __init__(self):
        self.velocidade = 0
    

    def acelerar(self):
        self.velocidade += 1
    

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
    



f1 = Carro('Norte', 10)
print(f1.direcao)
print(f1.calcular_velocidade)
