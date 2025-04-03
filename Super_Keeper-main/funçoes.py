import pygame
import sys
import random

pygame.init()
#Base da movimentação das bolas
def __init__(self, velocidade_base, dano, intervalo_base, imagem_path):
    self.v_base = velocidade_base
    self.intervalo_base = intervalo_base
    self.dano = dano
    self.timer = 0
    self.bolas = []
    # Carrega imagem específica da bola
    self.img = pygame.image.load(imagem_path).convert_alpha()
    self.img = pygame.transform.scale(self.img, (60, 60))


def velocidade_atual(self, pontos):
    return self.v_base + (self.v_base * pontos / 150)


def intervalo_atual(self, pontos):
    return max(10, int(self.intervalo_base - (pontos / 10)))

def spawn(self):
    rect = self.img.get_rect()
    rect.x = random.randint(0, largura - rect.width)
    rect.y = -rect.height
    self.bolas.append({"img": self.img, "rect": rect})

def atualizar(self, pontos):
    self.timer += 1
    if self.timer >= self.intervalo_atual(pontos):
        self.spawn()
        self.timer = 0

    novas_bolas = []
    for b in self.bolas:
        b["rect"].y += self.velocidade_atual(pontos)
        if b["rect"].top <= altura:
            novas_bolas.append(b)
    self.bolas = novas_bolas

def desenhar(self, tela):
    for b in self.bolas:
        tela.blit(b["img"], b["rect"])

def verificar_saidas(self):
    saidas = []
    novas_bolas = []
    for b in self.bolas:
        if b["rect"].top > altura:
            saidas.append(self.dano)
        else:
            novas_bolas.append(b)
    self.bolas = novas_bolas
    return saidas
#Def de cada bola
def __init__(self):
    super().__init__(velocidade_base=2, dano=1, intervalo_base=60, imagem_path="bola1.png")

def __init__(self):
    super().__init__(velocidade_base=4, dano=2, intervalo_base=80, imagem_path="bola2.png")

def __init__(self):
    super().__init__(velocidade_base=6, dano=3, intervalo_base=100, imagem_path="bola3.png")