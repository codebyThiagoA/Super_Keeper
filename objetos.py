import pygame as pg
from abc import ABC

#Classe para posições
class Positions(ABC):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

#Classe do goleiro
class Goalkeeper(Positions):
    def __init__(self, pos_x, pos_y, speed, width):
        super().__init__(pos_x, pos_y)
        self.speed = speed  # Velocidade de movimento lateral
        self.width = width  # Largura do goleiro (para colisão e limites)
        self.lives = 3  # Número inicial de vidas
        self.default_state = (pos_x, pos_y, speed, width, 3)  # Estado inicial para reinício
