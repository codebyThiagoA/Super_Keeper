import pygame

# Inicializa o mixer de som do Pygame
pygame.mixer.init()

# Sons
som_tela_inicial = pygame.mixer.Sound('audio/som_tela_inicial.wav')
som_estadio = 'audio/som_estadio.mp3'
som_perda_vida = pygame.mixer.Sound('audio/som_perda_vida.wav')
som_defesa = pygame.mixer.Sound('audio/som_defesa.wav')
som_derrota = pygame.mixer.Sound('audio/som_derrota.wav')
som_tela_derrota = 'audio/som_tela_derrota.mp3'

