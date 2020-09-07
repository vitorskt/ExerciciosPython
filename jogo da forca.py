import random

forcaing = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamburger chocolate giroscopio programador'.split()


def main():
    """
    Funcao Principal do programa
    """
    global forcaing
 
    print('F O R C A')
    letras_erradas = ''  # criamos uma string de letras erradas vazia
    letras_acertadas = ''  # string de letras acertadas vazia
    palavra_secreta = gera_palavra_aleatoria().upper()
    jogando = True
 
    while jogando:  # enquanto o usuario estiver jogando ou seja enquanto jogando for true
        imprime_jogo(letras_erradas, letras_acertadas, palavra_secreta)  # chama a funcao imprime jogo
 
        palpite = recebe_palpite(letras_erradas + letras_acertadas)
 
        if palpite in palavra_secreta:  # se o palpite for uma letra que ta na palavra certa
            letras_acertadas += palpite  # minhas letras certas terao que incrementar 1 + o palpite
 
            if verifica_se_ganhou(palavra_secreta, letras_acertadas):  # aqui a gente verifica se o jogo foi vencido
                print("Parabens! A palavra secreta é "+palavra_secreta+'! Voce ganhou!!')
                jogando = False
        else:
            letras_erradas += palpite
 
            if len(letras_erradas) == len(forcaing) - 1:
                imprime_jogo(letras_erradas, letras_acertadas, palavra_secreta)  # se sim vai ser imprimido o jogo
 
                print("Voce exagerou o seu limite de palpites!")
                print("Depois de "+str(len(letras_erradas))+' letras erradas e '+str(len(letras_acertadas)), end=' ')
                print('palpites corretos, a palavra era '+palavra_secreta+'.')
 
                jogando = False

        if not jogando:  # verifica se jogando e falso
            if jogar_novamente():
                letras_erradas = ''  # reinicio as letra erradas
                letras_acertadas = ''  # reinicia letras certas
                jogando = True
                palavra_secreta = gera_palavra_aleatoria().upper()  # ele vai gerar palavra aleatoria


def gera_palavra_aleatoria():
    """
    Funcao que retorna uma string a partir da
    lista de palavras global
    """
    global palavras
    return random.choice(palavras)


def imprime_com_espacos(palavra):
    """
    Recebe uma string palavra ou lista e imprime essa com
    espaco entre suas letras ou strings
    """
    for letra in palavra:
        print(letra, end=' ')
 
    print()
 

def imprime_jogo(letras_erradas, letras_acertadas, palavra_secreta):
    """
    Feito a partir da variavel global que contem as imagens
    do jogo em ASCII art, e tambem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta
    """
    global forcaing  # defi uma variavel global
    print(forcaing[len(letras_erradas)]+'\n')  # essa variavel ira receber a quantidade de letras erradas a ela
 
    print("Letras Erradas:", end=' ')  # estamos pedidndo todas as letras erradas que rebera um espaco entre elas
    imprime_com_espacos(letras_erradas)  # dai ele chama o metodo de espaco das letras erradas
 
    vazio = '_'*len(palavra_secreta)  # criando o espaco vazio, que vai ter o anderline como o mesmo numero de letras
    for i in range(len(palavra_secreta)):  # para cada acerto do usuario irremos percorrer o len da palavra
        if palavra_secreta[i] in letras_acertadas:  # verifica se o indice da palavra esta em letras
            vazio = vazio[:i] + palavra_secreta[i] + vazio[i+1:]
 
    imprime_com_espacos(vazio)  # chama o metodo para imprimir com espacos


def recebe_palpite(palpite_feitos):
    """ Essa funcao garante que o usuario digite so uma letra e que confere se a mesma ja foi chutada """
    
    while True:  # enquanto o palpiteFeitos for verdadeiro
        palpite = input('Adivinhe alguma letra. \n').upper()
        # aqui a variavel ira receber uma letra e passala para Maiuscula
        
        if len(palpite) != 1:  # verifica se apalavra escrita em palpite tem uma letra so.
            print('Coloque uma unica letra')
        elif palpite in palpite_feitos:  # se palpite esta dentro de palpites feitos
            print('Voce ja digitou essa letra, digite de novo!')
        elif not 'A' <= palpite <= 'Z':  # verifica se palpite e menor ou igual a A ou se e menor ou igual a Z
            print('Escolha Somente uma letra!')
        else:
            return palpite  # se estiver dentro dos conformes ele retorna o palpite


def jogar_novamente():
    """
    Funcao que pede para o usuario decidir se ele quer
    jogar novamente e retorna um booleano representando
    a resposta
    """
    return input("Voce quer jogar novamente? (sim ou nao)\n").upper().startswith('S')


def verifica_se_ganhou(palavra_secreta, letras_acertadas):
    """
    Funcao que verifica se o usuario acertou todas as
    letras da palavra secreta """
    
    ganhou = True
    for letra in palavra_secreta:
        if letra not in letras_acertadas:
            ganhou = False
            break
 
    return ganhou


main()
