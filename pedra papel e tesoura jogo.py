import time, random
print('BORA BRINCAR KK...')

time.sleep(1)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint (0, 2)

print('''Escolha sua jogada: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua escolha? '))
while jogador >= 3:
    print('JOGA DIREITO, TABACUDO!')
    jogador = int(input('Qual a sua escolha? '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')

print(':-' * 12)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print(':-' * 12)

if computador == 0: #pedra
    if jogador == 0:
        print (' O JOGO DEU EMPATE')
    elif jogador == 1:
        print ('O JOGADOR GANHOU, BICHO CAGÃO')
    elif jogador == 2:
        print ('PERDEU PRO PC KKKK!')
    else:
        print ('JOGA DIREITO, TABACUDO!')

elif computador == 1: #papel
    if jogador == 0:
        print ('PERDEU PRO PC, TEM NEM VERGONHA')
    elif jogador == 1:
        print ('O JOGO DEU EMPATE')
    elif jogador == 2:
        print ('O JOGADOR GANHOU, SORTUDO')
    else:
        print ('JOGA DIREITO, RETARDADO')    

elif computador == 2: #tesoura
    if jogador == 0:
        print ('O JOGADOR GANHOU NA CAGADA')    
    elif jogador == 1:
        print ('PERDEU PRO PC, AUGEEE')
    elif jogador == 2:
        print ('O JOGO DEU EMPATE')
    else:
        print ('SE N QUER JOGAR, VAZA')

    
