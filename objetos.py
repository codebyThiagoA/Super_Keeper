import pygame
import random  
import time
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN
from objetos import carregar_imagem, carregar_som
from objetos import LARGURA, ALTURA, TELA, TAMANHOS_FONTES, POSICOES_ESTATISTICAS, posicoes_coracoes, contadores, coracao, coracao_cinza, botao_jogar, botao_sair, botao_reiniciar, botao_sair_gameover

LARGURA, ALTURA = 800, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Super Keeper")
clock = pygame.time.Clock()

# Constantes
POSICOES_ESTATISTICAS = {
    'bola1': (325, 480), 'bola2': (455, 480), 'bola3': (585, 480),
    'tempo': (390, 400), 'score': (570, 400), 'total': (465, 300)
}
TAMANHOS_FONTES = {'total_bolas': 70, 'tempo/score': 60, 'bolas': 45}
posicoes_coracoes = [(650, 105), (675, 105), (700, 105), (725, 105), (750, 105)]
contadores = {
    'posicoes': {
        'bola1': (10, 15), 'bola2': (10, 60), 'bola3': (10, 105),
        'score': (665, 70), 'timer': (665, 15)
    }
}


# Classes
class BolaBase:
    def __init__(self, velocidade_base, dano, intervalo_base, imagem_path):
        self.v_base = velocidade_base
        self.dano = dano
        self.intervalo_base = intervalo_base
        self.timer = 0
        self.bolas = []
        self.img = carregar_imagem(imagem_path, (60, 60))

    def velocidade_atual(self, pontos):
        return self.v_base + (self.v_base * pontos / 150)

    def intervalo_atual(self, pontos):
        return max(10, int(self.intervalo_base - (pontos / 10)))

    def spawn(self):
        rect = self.img.get_rect()
        rect.x = random.randint(0, LARGURA - rect.width)
        rect.y = -rect.height
        return {"img": self.img, "rect": rect, "tipo": self}

    def atualizar(self, pontos):
        self.timer += 1
        dano_causado = 0
        if self.timer >= self.intervalo_atual(pontos):
            self.bolas.append(self.spawn())
            self.timer = 0
        novas_bolas = []
        for b in self.bolas:
            b["rect"].y += self.velocidade_atual(pontos)
            if b["rect"].top <= ALTURA:
                novas_bolas.append(b)
            else:
                dano_causado += self.dano
        self.bolas = novas_bolas
        return dano_causado

    def desenhar(self, tela):
        for b in self.bolas:
            tela.blit(b["img"], b["rect"])

class Goalkeeper:
    def __init__(self, posicao_x, posicao_y, speed, width, imagem_path):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.speed = speed
        self.width = width
        self.lives = 5
        self.img = carregar_imagem(imagem_path, (self.width, 100))

    @property
    def x(self):
        return self.posicao_x

    @property
    def y(self):
        return self.posicao_y

    def move(self, keys, screen_width):
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.posicao_x += self.speed
        if keys[pygame.K_LEFT] and self.x > 0:
            self.posicao_x -= self.speed

    def check_collision(self, ball_rect):
        goalkeeper_rect = pygame.Rect(self.x, self.y, self.width, 100)
        return goalkeeper_rect.colliderect(ball_rect)