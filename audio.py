import pygame

pygame.mixer.init()
som_tela_inicial = pygame.mixer.Sound('audio/som_tela_inicial.wav')
som_estadio = 'audio/som_estadio.mp3'
som_perda_vida = pygame.mixer.Sound('audio/som_perda_vida.wav')
som_defesa = pygame.mixer.Sound('audio/som_defesa.wav')
som_derrota = pygame.mixer.Sound('audio/som_derrota.wav')

def tocar_som_tela_inicial():
    som_tela_inicial.play()
def tocar_som_estadio():
    pygame.mixer.music.load(som_estadio)
    pygame.mixer.music.play(-1)  
def parar_som_estadio():
    pygame.mixer.music.stop()
def tocar_som_perda_vida():
    som_perda_vida.play()
def tocar_som_defesa():
    som_defesa.play()
def tocar_som_derrota():
    som_derrota.play()