import pygame as pg
from objetos import Goalkeeper, Ball
from sprite_sheet import sprite_sheet
from random import randint

pg.init() #Inicia a variavel init, e consequentemente todos os módulos do pygame
screen = pg.display.set_mode((800, 700)) #Cria a janela do jogo
clock = pg.time.Clock() #Inicia um relógio no jogo

#goalkeeper = Goalkeeper(x_screen/2 - sprite_sheet[3][0].get_width()//2, y_screen*0.9, 4, sprite_sheet[3][0].get_width())
onscreen = [Ball(x_screen/4, 0, 0, frame_count)]  # Exemplo: bola tipo 1 caindo

#goleiro
screen_width = screen.get_width() #Recebe a largura da tela
goalkeeper = Goalkeeper(screen_width // 2 - 50, 500, 5, 100) #Posição inicial do goleiro no centro
balls = []
frame_count = 0

running = True
while running: #loop principal

    for event in pg.event.get():

        if event.type == pg.QUIT:

            running = False #Para o looping do jogo se o jogador fechar

    keys = pg.key.get_pressed() #Armazena as teclas pressionadas pelo jogador
    goalkeeper.move(keys, screen_width) #Baseado nas teclas pressionadas, desloca o jogador pra esquerda ou pra direita

    if frame_count % 60 == 0:
        ball_x = randint(0, screen_width - 30)
        balls.append([sprite_sheet[0], ball_x, 0])  # [sprite, x, y]
    

    screen.fill((0, 128, 0))  #Background verde

    # Atualiza e desenha bolas
    for ball in balls[:]:
        ball[2] += 3  # Velocidade de queda
        ball_rect = sprite_sheet[0].get_rect(topleft=(ball[1], ball[2]))
        if goalkeeper.check_collision(ball_rect):
            balls.remove(ball)  # Remove bola ao colidir
        elif ball[2] > screen.get_height():
            balls.remove(ball)
            goalkeeper.lose_life()  # Perde vida se a bola passar
        else:
            screen.blit(ball[0], (ball[1], ball[2]))


    #pg.draw.rect(screen, (0, 0, 255), (goalkeeper.x, goalkeeper.y, goalkeeper.width, 50))  #Desenha um goleiro provisorio azul

    goalkeeper.draw(screen)
    pg.display.update() #Atualiza na tela as posições dos objtos
    frame_count += 1
    clock.tick(120)#FPS do game

pg.quit()