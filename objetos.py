import pygame as pg
from abc import ABC

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
        self.default_state = (posicao_x, posicao_y, speed, width, 4)  #Tupla com o Estado inicial do goleiro
