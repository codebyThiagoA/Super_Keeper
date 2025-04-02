import pygame

# Inicializa o Pygame
pygame.init()

# Definições da tela
LARGURA, ALTURA = 800, 600
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
coracao = pygame.transform.scale(coracao, (40, 40))

# Posições dos corações
posicoes_coracoes = [(650, 20), (700, 20), (750, 20)]

def tela_jogo():
    """Tela do jogo principal."""
    jogando = True
    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Desenha a tela do jogo
        TELA.blit(fundo_jogo, (0, 0))
        
        # Desenha os corações na tela
        for posicao in posicoes_coracoes:
            TELA.blit(coracao, posicao)
        
        pygame.display.flip()

def tela_inicial():
    """Tela inicial do jogo."""
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar_rect.collidepoint(evento.pos):
                    tela_jogo()  # Muda para a tela do jogo
                if botao_sair_rect.collidepoint(evento.pos):
                    rodando = False
        
        # Desenha a tela inicial
        TELA.blit(fundo_inicial, (0, 0))
        TELA.blit(botao_jogar, botao_jogar_rect.topleft)
        TELA.blit(botao_sair, botao_sair_rect.topleft)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    tela_inicial()
