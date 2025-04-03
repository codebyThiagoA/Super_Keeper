import pygame as pg
from objetos import Goalkeeper
from sprite_sheet import sprite_sheet

pg.init() #Inicia a variavel init, e consequentemente todos os módulos do pygame
screen = pg.display.set_mode((800, 700)) #Cria a janela do jogo
clock = pg.time.Clock() #Inicia um relógio no jogo
frame_count = 0

#goleiro
screen_width = screen.get_width() #Recebe a largura da tela
goalkeeper = Goalkeeper(screen_width // 2 - 50, 500, 5, 100) #Posição inicial do goleiro no centro

running = True

while running: #loop principal

    for event in pg.event.get():

        if event.type == pg.QUIT:

            running = False #Para o looping do jogo se o jogador fechar

    keys = pg.key.get_pressed() #Armazena as teclas pressionadas pelo jogador
    goalkeeper.move(keys, screen_width) #Baseado nas teclas pressionadas, desloca o jogador pra esquerda ou pra direita

    screen.fill((0, 128, 0))  #Background verde
    #pg.draw.rect(screen, (0, 0, 255), (goalkeeper.x, goalkeeper.y, goalkeeper.width, 50))  #Desenha um goleiro provisorio azul

    goalkeeper.draw(screen)
    pg.display.update() #Atualiza na tela as posições dos objtos
    frame_count += 1
    clock.tick(120)#FPS do game

pg.quit()