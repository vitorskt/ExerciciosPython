class Pessoa:

    def __init__(self, nome, idade, sexo, comendo=False, falando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print('{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return #f'{self.nome} não está falando'
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} está comendo {comida}')
        self.comendo = True
        return

    def parar_comer(self):
        if not self.comendo:
            print('{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
        return


p1 = Pessoa('Vitor', 19, 'Masculino')
p2 = Pessoa('Laura', 19, 'Feminino')

p1.parar_falar()
#print(p1.parar_falar())