
som_tela_inicial = pygame.mixer.Sound('audio/som_tela_inicial.wav')
#if estiver na tela inicial
som_tela_inicial.play()



#if estiver na tela de jogo
som_estadio = pygame.mixer.music.load('audio/som_estadio.mp3')
pygame.mixer.music.play(-1)



som_perda_vida = pygame.mixer.Sound('audio/som_perda_vida.wav')
#if gol acontecer
som_perda_vida.play()



som_defesa = pygame.mixer.Sound('audio/som_defesa.wav')
#if goleiro defender 
som_defesa.play()



som_derrota = pygame.mixer.Sound('audio/som_derrota.wav')
#if player perder
som_derrota.play()



#if estiver na tela de game over
som_tela_derrota = pygame.mixer.music.load('audio/som_tela_derrota.mp3')
pygame.mixer.music.play(-1)

