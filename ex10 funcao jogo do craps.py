from random import choice

print('=== JOGO DO CRAPS ===')

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pontuacao = 0
inicio = input('digite[jogar] para entrar no jogo ou\n[sair] para sair do jogo: ').strip().lower()
while True:
    if inicio == 'sair':
        exit()
    else:
        jogada = input('digite [OK] para fazer sua jogada: ').strip().lower()
        if jogada == 'ok':
            res1 = choice(dados)
            print(f'=-=-=-= Os dados resultou em {res1} =-=-=-=')
            if res1 == 7 or res1 == 11:
                print('=-=-=-= Os dados resultou em um NATURAL, Parabéns, você venceu!!! =-=-=-=')
            elif res1 == 2 or res1 == 3 or res1 == 12:
                print('=-=-=-= Os dados resultou em um CRAPS, você PERDEU!! =-=-=-=')
                pontuacao = 0
            elif res1 == 4 or res1 == 5 or res1 == 6 or res1 == 8 or res1 == 9 or res1 == 10:
                pontuacao += res1
                print(f'=-=-=-= Este é seu ponto. Sua pontuação agora é {pontuacao} =-=-=-=')
                res1 = input('digite [OK] para jogar novamente\nou [sair] para sair do jogo: ').strip().lower()
                if res1 == 'sair':
                    exit()
                    break
                elif res1 == 'ok':
                    res1 = choice(dados)
                    pontuacao+= res1
                    print(f'=-=-=-= Os dados resultou em {res1} =-=-=-=')
                    if res1 == 7:
                        print('=-=-=-= seu dado resultou em 7, você perdeu =-=-=-=')
                        pontuacao = 0
                    elif res1 == 2 or res1 == 3 or res1 == 12:
                        print('=-=-=-= Os dados resultou em um CRAPS, você PERDEU!! =-=-=-=')
                        pontuacao = 0
                    else:
                        print(f'=-=-=-= Este é seu ponto. Sua pontuação agora é {pontuacao} =-=-=-=')
                        
