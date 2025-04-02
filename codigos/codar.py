import pygame
import time

# Inicializa o Pygame
pygame.init()

# Definições da tela
LARGURA, ALTURA = 800, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela Básica do Pygame")

# Carregar imagens da tela inicial
fundo_inicial = pygame.image.load(r"designs/Tela_inicial.png")
fundo_inicial = pygame.transform.scale(fundo_inicial, (LARGURA, ALTURA))

botao_jogar = pygame.image.load(r"designs/Botao_jogar.png")
botao_jogar_rect = botao_jogar.get_rect(topleft=(20, 280))

botao_sair = pygame.image.load(r"designs/Botao_sair.png")
botao_sair_rect = botao_sair.get_rect(topleft=(20, 410))

# Carregar imagens da tela do jogo
fundo_jogo = pygame.image.load(r"designs/Campo.png")
fundo_jogo = pygame.transform.scale(fundo_jogo, (LARGURA, ALTURA))

# Carregar imagem dos corações
coracao = pygame.image.load(r"designs/Coracao.png")
coracao = pygame.transform.scale(coracao, (30, 30))

# Carregar imagem do timer
timer_img = pygame.image.load(r"designs/Relogio.png")
timer_img = pygame.transform.scale(timer_img, (100, 40))  # Ajusta tamanho

bola1_img = pygame.image.load(r"designs/Contador_bola1.png")
bola1_img = pygame.transform.scale(bola1_img, (100, 40))

bola2_img = pygame.image.load(r"designs/Contador_bola2.png")
bola2_img = pygame.transform.scale(bola2_img, (100, 40))

bola3_img = pygame.image.load(r"designs/Contador_bola3.png")
bola3_img = pygame.transform.scale(bola3_img, (100, 40))

# Posições 
posicoes_coracoes = [(650, 105), (675, 105), (700, 105), (725, 105), (750, 105)]
posicao_contadorbola1 = (10, 15)
posicao_contadorbola2 = (10, 60)
posicao_contadorbola3 = (10, 105)
posicao_score = (665, 70)
posicao_timer = (665, 15)

# Fonte para exibir o tempo e a pontuação
fonte = pygame.font.Font(None, 36)

def tela_jogo():
    """Tela do jogo principal."""
    inicio_tempo = time.time()  # Marca o tempo de início
    pontos = 0  # Inicializa a pontuação
    contador_bola1 = 0
    contador_bola2 = 0
    contador_bola3 = 0
    jogando = True
    while jogando:
        tempo_decorrido = int(time.time() - inicio_tempo)  # Calcula tempo decorrido
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return  # Retorna para a tela inicial sem fechar o jogo

        # Desenha a tela do jogo
        TELA.blit(fundo_jogo, (0, 0))

        # Desenha os corações na tela
        for posicao in posicoes_coracoes:
            TELA.blit(coracao, posicao)

        # Desenha os contadores na tela
        TELA.blit(timer_img, posicao_timer)
        TELA.blit(bola1_img, posicao_contadorbola1)
        TELA.blit(bola2_img, posicao_contadorbola2)
        TELA.blit(bola3_img, posicao_contadorbola3)

        # Renderiza e exibe as informações na tela
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
                    tela_jogo()  # Muda para a tela do jogo
                if botao_sair_rect.collidepoint(evento.pos):
                    pygame.quit()
                    return  # Fecha o jogo corretamente

        # Desenha a tela inicial
        TELA.blit(fundo_inicial, (0, 0))
        TELA.blit(botao_jogar, botao_jogar_rect.topleft)
        TELA.blit(botao_sair, botao_sair_rect.topleft)

        pygame.display.flip()

if __name__ == "__main__":
    tela_inicial()