import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura_tela = 980
altura_tela = 720
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Variáveis do jogo
velocidade_bola = [4, 4]
posicao_bola = [largura_tela // 2, altura_tela // 2]
raquete_largura = 10
raquete_altura = 100
posicao_raquete1 = [50, altura_tela // 2 - raquete_altura // 2]
posicao_raquete2 = [largura_tela - 50 - raquete_largura, altura_tela // 2 - raquete_altura // 2]
velocidade_raquete = 10

# Variáveis de pontuação
pontuacao_jogador1 = 0
pontuacao_jogador2 = 0

# Fonte para o placar
fonte = pygame.font.Font(None, 74)

# Função para exibir o placar
def mostrar_placar():
    texto = fonte.render(f"{pontuacao_jogador1} - {pontuacao_jogador2}", True, branco)
    tela.blit(texto, (largura_tela // 2 - texto.get_width() // 2, 10))

# Função principal do jogo
def jogo():
    global posicao_bola, velocidade_bola, pontuacao_jogador1, pontuacao_jogador2

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimenta as raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            posicao_raquete1[1] -= velocidade_raquete
        if teclas[pygame.K_s]:
            posicao_raquete1[1] += velocidade_raquete
        if teclas[pygame.K_UP]:
            posicao_raquete2[1] -= velocidade_raquete
        if teclas[pygame.K_DOWN]:
            posicao_raquete2[1] += velocidade_raquete

        # Atualiza a posição da bola
        posicao_bola[0] += velocidade_bola[0]
        posicao_bola[1] += velocidade_bola[1]

        # Verifica colisão com as paredes
        if posicao_bola[1] <= 0 or posicao_bola[1] >= altura_tela:
            velocidade_bola[1] = -velocidade_bola[1]

        # Verifica colisão com as raquetes
        if (posicao_bola[0] <= posicao_raquete1[0] + raquete_largura and
            posicao_raquete1[1] <= posicao_bola[1] <= posicao_raquete1[1] + raquete_altura):
            velocidade_bola[0] = -velocidade_bola[0]

        if (posicao_bola[0] >= posicao_raquete2[0] - raquete_largura and
            posicao_raquete2[1] <= posicao_bola[1] <= posicao_raquete2[1] + raquete_altura):
            velocidade_bola[0] = -velocidade_bola[0]

        # Verifica se a bola saiu da tela
        if posicao_bola[0] <= 0:
            pontuacao_jogador2 += 1
            posicao_bola = [largura_tela // 2, altura_tela // 2]
            velocidade_bola[0] = -velocidade_bola[0]
        elif posicao_bola[0] >= largura_tela:
            pontuacao_jogador1 += 1
            posicao_bola = [largura_tela // 2, altura_tela // 2]
            velocidade_bola[0] = -velocidade_bola[0]

        # Desenha tudo na tela
        tela.fill(preto)
        pygame.draw.rect(tela, branco, (*posicao_raquete1, raquete_largura, raquete_altura))
        pygame.draw.rect(tela, branco, (*posicao_raquete2, raquete_largura, raquete_altura))
        pygame.draw.ellipse(tela, branco, (*posicao_bola, 20, 20))
        pygame.draw.aaline(tela, branco, (largura_tela // 2, 0), (largura_tela // 2, altura_tela))

        # Mostrar o placar
        mostrar_placar()

        # Atualiza a tela
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Inicia o jogo
jogo()
