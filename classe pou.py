class Pou:

    def __init__(self, nome, idade=1, comendo=False, dormindo=False, brincando=False, conversando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.dormindo = dormindo
        self.conversando = conversando
        self.brincando = brincando
    

    def falar(self,assunto):
        if self.conversando:
            return f'{self.nome} já está conversando'
        elif self.comendo:
            return f'{self.nome} não pode falar comendo'
        elif self.dormindo:
            return f'{self.nome} não consegue falar dormindo'
        else:
            self.conversando = True
            return f'{self.nome} começou a conversar sobre {assunto}'
    

    def parar_falar(self):
        if not self.conversando:
            return f'{self.nome} não está falando'
        else:
            self.conversando = False
            return f'{self.nome} parou de falar'
        
    
    def comer(self, alimento):
        if self.comendo:
            return f'{self.nome} já está comendo!'
        elif self.conversando:
            return f'{self.nome} não pode comer conversando!'
        elif self.dormindo:
            return f'{self.nome} não consegue comer dormindo!'
        else:
            self.comendo = True
            return f'{self.nome} começou a comer {alimento}.'
        
    
    def parar_comer(self):
        if not self.comendo:
            return f'{self.nome} não está comendo!'
        else:
            self.comendo = False
            return f'{self.nome} parou de comer.'
    

    def dormir(self):
        if self.dormindo:
            return f'{self.nome} já está dormindo!'
        elif self.comendo:
            return f'{self.nome} precisa parar de comer para poder dormir!'
        elif self.brincando:
            return f'{self.nome} precisa parar de brincar para poder dormir!'
        else:
            self.dormindo = True
            return f'{self.nome} foi dormir.'
    

    def acordar(self):
        if not self.dormindo:
            return f'{self.nome} já está acordado!!'
        else:
            self.dormindo = False
            return f'{self.nome} acordou!'
    
    def brincar(self, brincadeira):
        if self.comendo:
            return f'{self.nome} não pode brincar, pois está comendo!'
        elif self.brincando:
            return f'{self.nome} já está brincando!'
        elif self.dormindo:
            return f'{self.nome} não pode brincar, pois está dormindo!!'
        else:
            self.brincando = True
            return f'{self.nome} começou a brincar de {brincadeira}.'
    
    def parar_brincar(self):
        if not self.brincando:
            return f'{self.nome} não está brincando.'
        else:
            self.brincando = False
            return f'{self.nome} parou de brincar!'



