import pygame
import time

# Inicializa o Pygame
pygame.init()

# Definições da tela
LARGURA, ALTURA = 800, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela Básica do Pygame")

# Carregar imagens da tela inicial
fundo_inicial = pygame.image.load("designs/Tela_inicial.png")
fundo_inicial = pygame.transform.scale(fundo_inicial, (LARGURA, ALTURA))

botao_jogar = pygame.image.load("designs/Botao_jogar.png")
botao_jogar_rect = botao_jogar.get_rect(topleft=(20, 280))

botao_sair = pygame.image.load("designs/Botao_sair.png")
botao_sair_rect = botao_sair.get_rect(topleft=(20, 410))

# Carregar imagens da tela do jogo
fundo_jogo = pygame.image.load("designs/Campo.png")
fundo_jogo = pygame.transform.scale(fundo_jogo, (LARGURA, ALTURA))

# Carregar imagens dos corações
coracao = pygame.image.load("designs/Coracao.png")
coracao = pygame.transform.scale(coracao, (30, 30))
coracao_cinza = pygame.image.load("designs/Coracao_perdido.png")
coracao_cinza = pygame.transform.scale(coracao_cinza, (30, 30))

# Carregar imagem do timer e contadores
timer_img = pygame.image.load("designs/Relogio.png")
timer_img = pygame.transform.scale(timer_img, (100, 40))

bola1_img = pygame.image.load("designs/Contador_bola1.png")
bola1_img = pygame.transform.scale(bola1_img, (100, 40))

bola2_img = pygame.image.load("designs/Contador_bola2.png")
bola2_img = pygame.transform.scale(bola2_img, (100, 40))

bola3_img = pygame.image.load("designs/Contador_bola3.png")
bola3_img = pygame.transform.scale(bola3_img, (100, 40))

# Carregar imagens da tela de Game Over
fundo_gameover = pygame.image.load("designs/Gameover.png")
fundo_gameover = pygame.transform.scale(fundo_gameover, (LARGURA, ALTURA))

botao_reiniciar = pygame.image.load("designs/Botao_jogar_novamente.png")
botao_reiniciar_rect = botao_reiniciar.get_rect(center=(LARGURA // 2, ALTURA // 2 + 200))
botao_sair_gameover = botao_sair.get_rect(center=(LARGURA // 2, ALTURA // 2 + 270))

# Posições 
posicoes_coracoes = [(650, 105), (675, 105), (700, 105), (725, 105), (750, 105)]
coracoes_visiveis = [True] * len(posicoes_coracoes)  # Estado dos corações

posicao_contadorbola1 = (10, 15)
posicao_contadorbola2 = (10, 60)
posicao_contadorbola3 = (10, 105)
posicao_score = (665, 70)
posicao_timer = (665, 15)

# Fonte para exibir o tempo e a pontuação
fonte = pygame.font.Font(None, 36)

def tela_gameover():
    """Tela de Game Over com opção de reiniciar o jogo."""
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar_rect.collidepoint(evento.pos):
                    tela_jogo()  # Reinicia o jogo
                elif botao_sair_gameover.collidepoint(evento.pos):
                    pygame.quit()
                    return
        
        TELA.blit(fundo_gameover, (0, 0))
        TELA.blit(botao_reiniciar, botao_reiniciar_rect.topleft)
        TELA.blit(botao_sair, botao_sair_gameover.topleft)
        pygame.display.flip()

def tela_jogo():
    """Tela do jogo principal."""
    global coracoes_visiveis  # Resetar os corações ao reiniciar o jogo
    coracoes_visiveis = [True] * len(posicoes_coracoes)

    inicio_tempo = time.time()
    pontos = 0
    contador_bola1 = 0
    contador_bola2 = 0
    contador_bola3 = 0
    coracoes_restantes = len(coracoes_visiveis)
    jogando = True

    while jogando:
        tempo_decorrido = int(time.time() - inicio_tempo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and coracoes_restantes > 0:
                    coracoes_visiveis[coracoes_restantes - 1] = False
                    coracoes_restantes -= 1

        # Se todos os corações forem perdidos, ir para a tela de Game Over
        if coracoes_restantes == 0:
            tela_gameover()
            return

        TELA.blit(fundo_jogo, (0, 0))

        for i, posicao in enumerate(posicoes_coracoes):
            if coracoes_visiveis[i]:
                TELA.blit(coracao, posicao)
            else:
                TELA.blit(coracao_cinza, posicao)

        TELA.blit(timer_img, posicao_timer)
        TELA.blit(bola1_img, posicao_contadorbola1)
        TELA.blit(bola2_img, posicao_contadorbola2)
        TELA.blit(bola3_img, posicao_contadorbola3)

        texto_tempo = fonte.render(f"{tempo_decorrido}", True, (255, 255, 255))
        texto_pontos = fonte.render(f"Score: {pontos}", True, (255, 255, 255))
        texto_bola1 = fonte.render(f"{contador_bola1}", True, (255, 255, 255))
        texto_bola2 = fonte.render(f"{contador_bola2}", True, (255, 255, 255))
        texto_bola3 = fonte.render(f"{contador_bola3}", True, (255, 255, 255))
        
        TELA.blit(texto_tempo, (posicao_timer[0] + 50, posicao_timer[1] + 10))
        TELA.blit(texto_pontos, (posicao_score[0], posicao_score[1]))
        TELA.blit(texto_bola1, (posicao_contadorbola1[0] + 50, posicao_contadorbola1[1] + 10))
        TELA.blit(texto_bola2, (posicao_contadorbola2[0] + 50, posicao_contadorbola2[1] + 10))
        TELA.blit(texto_bola3, (posicao_contadorbola3[0] + 50, posicao_contadorbola3[1] + 10))
        
        pygame.display.flip()

def tela_inicial():
    """Tela inicial do jogo."""
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar_rect.collidepoint(evento.pos):
                    tela_jogo()
                if botao_sair_rect.collidepoint(evento.pos):
                    pygame.quit()
                    return
        
        TELA.blit(fundo_inicial, (0, 0))
        TELA.blit(botao_jogar, botao_jogar_rect.topleft)
        TELA.blit(botao_sair, botao_sair_rect.topleft)

        pygame.display.flip()

if __name__ == "__main__":
    tela_inicial()
