"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível resultadotante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class Bombacombustivel:


    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel=0):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    
    def abastecer_por_valor(self, valor):
        resultado = valor / self.valor_litro
        self.quant_combustivel -= resultado
        return f'Valor pago R${valor}, quantidade abastecida: {resultado:.2f}L'
        
    
    def abastecer_por_litro(self, valor):
        resultado = valor * self.valor_litro
        self.quant_combustivel -= resultado
        return f'Valor pago R${valor}, quantidade abastecida: {resultado}L'

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quant_combustivel(self, quantidade):
        self.quant_combustivel = quantidade




b1 = Bombacombustivel('gasolina', 5.20, 20)
print(b1.abastecer_por_valor(20))

        

    
