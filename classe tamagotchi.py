class Tamagotchi:

    def __init__(self, nome, bucho=[], comendo=False, brincando=False):
        self.nome = nome
        self.bucho = []
        self.comendo = comendo
        self.brincando = brincando


    def comer(self, alimento):
        if self.comendo:
            return f'O tamagotchi {self.nome} já está comendo'
        elif self.brincando:
            return f'O tamagotchi {self.nome} não pode comer brincando'
        self.bucho.append(alimento)
        self.comendo = True
        return f'O tamagotchi {self.nome} está comendo {alimento}'


    def parar_comer(self):
        if not self.comendo:
            return f'O tamagotchi {self.nome} não está comendo'
        self.comendo = False
        return f'O tamagotchi {self.nome} parou de comer'


    def ver_bucho(self):
        return self.bucho
    

    def digestao(self):
        self.bucho.clear()
        return self.digestao

    
    def brincar(self, brincadeira):
        if self.comendo:
            return f'O tamagotchi {self.nome} não pode brincar comendo'
        self.brincando = True
        return f'O tamagotchi {self.nome} está brincando de {brincadeira}'
    
    def parar_brincar(self):
        if not self.brincando:
            return f'O tamagotchi {self.nome} não está brincando'
        self.brincando = False
        return f'O tamagotchi {self.nome} parou de brincar'


t1 = Tamagotchi('Vitor')
print(t1.comer('carne'))
print(t1.parar_comer())
print(t1.brincar('Bola'))
t1.digestao()
print(t1.ver_bucho())