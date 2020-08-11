class Carro:
    def __init__(self,propietario, marca,litros=0,andando=False,abastecendo=False):
        self.propietario = propietario
        self.marca = marca
        self.litros = litros
        self.andando = andando
        self.abastecendo = abastecendo

        
    def dirigir(self,km):
        if self.litros == 0:
            print('Carro sem gasolina')
            return
        if self.andando:
            print('O carro já está andando.')
            return
        print('Você começou a digitir o carro.')
        self.andando = True
        self.litros /= 4

    def parar_dirigir(self):
        if not self.andando:
            print('O carro está parado.')
            return
        print('Você parou de dirigir.')
        self.andando = False


    def abastecer(self,litros):
        if self.andando:
            print('Não pode abastecer com o carro em movimento')
            return
        print(f'Abasteceu {litros}L.')
        self.litros += litros


c1 = Carro('Vitor', 'Ferrari')

c1.abastecer(70)
c1.dirigir(100)
c1.parar_dirigir()
c1.parar_dirigir()
