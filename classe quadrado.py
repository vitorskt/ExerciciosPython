class Quadrado:
    def __init__(self,tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self,x):
        self.tamanho_lado = x
        print(f'Novo valor = {x}')

    def valorlado(self):
        print(f'Valor do lado = {self.tamanho_lado}')

    def calcular_area(self):
        print('Área = {}cm²'.format(self.tamanho_lado**2))


q1 = Quadrado(4.5)

q1.valorlado()
q1.mudar_valor_lado(6)
q1.calcular_area()

