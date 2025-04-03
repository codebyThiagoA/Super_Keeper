import pygame
import sys
import random
from pygame.locals import *  # Importa constantes como K_a, K_LEFT, etc.

pygame.init()

altura, largura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bolas com Imagens Diferentes")

branco = (255, 255, 255)
clock = pygame.time.Clock()

# Variáveis do jogador (objeto azul)
pos_azul_x = largura // 2
pos_azul_y = altura - 70
velocidade_azul = 5
tamanho_azul = 50
cor_azul = (0, 0, 255)  # Azul

# Classe base de comportamento
class BolaBase:
    def __init__(self, velocidade_base, dano, intervalo_base, imagem_path):
        self.v_base = velocidade_base
        self.intervalo_base = intervalo_base
        self.dano = dano
        self.timer = 0
        self.bolas = []

        # Carrega imagem específica da bola
        try:
            self.img = pygame.image.load(imagem_path).convert_alpha()
            self.img = pygame.transform.scale(self.img, (60, 60))
        except:
            # Se a imagem não carregar, cria uma superfície colorida
            self.img = pygame.Surface((60, 60), pygame.SRCALPHA)
            cor = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            pygame.draw.circle(self.img, cor, (30, 30), 30)

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
    
    def verificar_colisoes(self, jogador_rect):
        colisoes = []
        novas_bolas = []
        for b in self.bolas:
            if b["rect"].colliderect(jogador_rect):
                colisoes.append(self.dano)
            else:
                novas_bolas.append(b)
        self.bolas = novas_bolas
        return colisoes

# Classes específicas com imagens próprias
class Bola1(BolaBase):
    def __init__(self):
        super().__init__(velocidade_base=2, dano=1, intervalo_base=60, imagem_path="bola1.png")

class Bola2(BolaBase):
    def __init__(self):
        super().__init__(velocidade_base=4, dano=2, intervalo_base=80, imagem_path="bola2.png")

class Bola3(BolaBase):
    def __init__(self):
        super().__init__(velocidade_base=6, dano=3, intervalo_base=100, imagem_path="bola3.png")

# Instanciar bolas
bola1 = Bola1()
bola2 = Bola2()
bola3 = Bola3()

vidas = 10
pontos = 0

rodando = True
while rodando and vidas > 0:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[K_a] or teclas[K_LEFT]:
        pos_azul_x -= velocidade_azul
    if teclas[K_d] or teclas[K_RIGHT]:
        pos_azul_x += velocidade_azul
    
    # Limitar jogador dentro da tela
    pos_azul_x = max(0, min(largura - tamanho_azul, pos_azul_x))

    # Atualização
    bola1.atualizar(pontos)
    bola2.atualizar(pontos)
    bola3.atualizar(pontos)

    # Verificar saídas
    for dano in bola1.verificar_saidas() + bola2.verificar_saidas() + bola3.verificar_saidas():
        vidas -= dano
        pontos += dano * 10
    
    # Verificar colisões com o jogador
    jogador_rect = pygame.Rect(pos_azul_x, pos_azul_y, tamanho_azul, tamanho_azul)
    for dano in bola1.verificar_colisoes(jogador_rect) + bola2.verificar_colisoes(jogador_rect) + bola3.verificar_colisoes(jogador_rect):
        pontos += dano * 20

    # Desenhar
    tela.fill(branco)
    bola1.desenhar(tela)
    bola2.desenhar(tela)
    bola3.desenhar(tela)
    
    # Desenhar jogador
    pygame.draw.rect(tela, cor_azul, (pos_azul_x, pos_azul_y, tamanho_azul, tamanho_azul))
    
    # Mostrar vidas e pontos
    fonte = pygame.font.SysFont(None, 36)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, (0, 0, 0))
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (0, 0, 0))
    tela.blit(texto_vidas, (10, 10))
    tela.blit(texto_pontos, (10, 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()