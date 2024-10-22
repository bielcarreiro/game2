import random

# Gerando os resultados dos dados
lado1 = random.randint(1, 6)
lado2 = random.randint(1, 6)
tentativas = 3

# Mensagem de boas vindas
print('Bem-vindo jogador ao Jogo de Dados! Insira um número de 1 a 6 duas vezes e tente acertar o lado certo que o dado caiu.')

# Receber os palpites dos jogadores
while tentativas > 0:
    palpite1 = int(input('Digite um número de 1 a 6: '))
    palpite2 = int(input('Digite um número de 1 a 6: '))

    # Verificando se os palpites estão corretos
    if palpite1 == lado1 and palpite2 == lado2:
        print('Parabéns jogador! Você ganhou um cookie.')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'Errado! Você tem {tentativas} tentativas restantes.')

    # Ajuda para acompanhar o jogador
    if palpite1 == lado1:
        print('Você acertou o primeiro dado.')
    elif palpite1 < lado1:
        print('Você errou o primeiro dado, tente um número mais alto.')
    elif palpite1 > lado1:
        print('Você errou o primeiro dado, tente um número mais baixo.')

    if palpite2 == lado2:
        print('Você acertou o segundo dado.')
    elif palpite2 < lado2:
        print('Você errou o segundo dado, tente um número mais alto.')
    elif palpite2 > lado2:
        print('Você errou o segundo dado, tente um número mais baixo.')

# GAME OVER
if tentativas == 0:
    print(f'Você perdeu, os lados corretos eram: {lado1} e {lado2}')

# Mensagem de despedida
print('Espero que tenham gostado do meu mini-game, até breve.')
