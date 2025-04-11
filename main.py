# coding: utf-8
import pygame
from functions import tela_inicial, tela_intermediaria, tela_gameover, tela_jogo
from configs import LARGURA, ALTURA, TELA, contadores, clock

pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Super Keeper")
clock = pygame.time.Clock()

def main():
    while True:
        # Chama a tela inicial
        tela_inicial()

        # Chama a tela intermediária (se necessário)
        tela_intermediaria()

        # Inicia o jogo
        tela_jogo()

        # Após o jogo terminar, exibe a tela de game over
        tela_gameover()

if __name__ == "__main__":
    main()