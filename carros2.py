class Carros:

    def __init__(self,marca, combustivel=0, andando=False):
        self.marca = marca
        self.combustivel = combustivel
        self.andando = andando

    def andar(self, km):
        if self.combustivel == 0:
            return f'Carro sem combustível'
        else:
            self.andando = True
            return f'Combustível restante {self.combustivel - (km/4)}L'

    def parar_andar(self):
        if not self.andando:
            return f'O carro já está parado'
        else:
            self.andando = False
            return f'O carro parou'
    

    def obter_gasolina(self):
        return f'Quantidade atual: {self.combustivel}L'

    def add_gasolina(self, quantidade):
        if self.andando:
            return f'O carro não pode abastecer andando'
        else:
            self.combustivel += quantidade
            return f'Abastecimento efetuado com sucesso'
    


"""meuFusca = Carros('Fusca')
print(meuFusca.andar(50))
meuFusca.add_gasolina(50)
print(meuFusca.andar(50))
meuFusca.parar_andar()
print(meuFusca.obter_gasolina())"""
