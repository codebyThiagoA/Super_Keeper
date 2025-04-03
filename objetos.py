import pygame as pg
from abc import ABC
from sprite_sheet import sprite_sheet

class Positions(ABC): #Classe abstrata para posições

    def __init__(self, posicao_x, posicao_y):

        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

class Goalkeeper(Positions): #Classe do goleiro

    def __init__(self, posicao_x, posicao_y, speed, width):

        super().__init__(posicao_x, posicao_y)
        self.speed = speed  #Velocidade de movimento lateral
        self.width = width  #Largura do goleiro (colisao e limites)
        self.lives = 4  #Vidas iniciais
        self.default_state = (posicao_x, posicao_y, speed, width, 4) #Tupla com o Estado inicial do goleiro
        self.sprite = pg.transform.scale(sprite_sheet[1][0], (self.width, self.width)) # sprite inicial do goleiro com ajuste de escala do personagem

    #convenções
    @property
    def x(self):
        return self.posicao_x

    @property
    def y(self):
        return self.posicao_y
    
    @property
    def _lives(self):
        return self.lives

    #Movimentação do goleiro 
    def move(self, keys, screen_width): #keys: teclas apertadas, screen_width: largura da tela

        if keys[pg.K_RIGHT] and self.x < screen_width - self.width: # caso a tecla da seta pra direita for apertada e o goleiro ão passar a borda

            self.posicao_x += self.speed #goleiro se move p direita
            if self.x > screen_width - self.width: #Caso ele ultrapasse a borda, ele mantém a posição na borda

                self.posicao_x = screen_width - self.width

        if keys[pg.K_LEFT] and self.x > 0: #Mesmo if identado, mas pra a tecla da esquerda

            self.posicao_x -= self.speed #goleiro se move p esquerda
            if self.x < 0: #Caso ele ultrapasse a borda, ele mantém a posição na borda

                self.posicao_x = 0

    #Identificar a bola (função do pygame)
    def check_collision(self, ball_rect):

        goalkeeper_rect = pg.Rect(self.x, self.y, self.width, 100) #teste com retangulo para representar o goleiro
        return goalkeeper_rect.colliderect(ball_rect)

    #Perca de vida
    def lose_life(self):

        self.lives -= 1 #desconta a vida
        return self.lives

    #Reiniciar o goleiro após perca de vida
    def restart(self):
        
        self.posicao_x, self.posicao_y, self.speed, self.width, self.lives = self.default_state

    def draw(self, screen): #integra a sprite do goleiro
        screen.blit(self.sprite, (self.x, self.y)) 
