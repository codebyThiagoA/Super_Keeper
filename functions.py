import pygame
from configs import *
from audio import tocar_som_estadio
from designs import carregar_imagem

def tela_intermediaria():
    fundo_intermediario = carregar_imagem("designs/Tela_intermediaria.png", (LARGURA, ALTURA))
    while True:
        for evento in pygame.event.get():
            pygame.mixer.music.set_volume(0.67) 
            tocar_som_estadio()
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return  # Sai da tela intermediária e continua para o jogo
        TELA.blit(fundo_intermediario, (0, 0))
        pygame.display.flip()

