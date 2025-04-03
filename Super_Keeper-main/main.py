import pygame
import sys
import random

pygame.init()

altura, largura= 800,600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bolas com Imagens Diferentes")

branco = (255, 255, 255)
clock = pygame.time.Clock()

# Classe base de comportamento
class BolaBase:
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

    # Atualização
    bola1.atualizar(pontos)
    bola2.atualizar(pontos)
    bola3.atualizar(pontos)

    # Verificar saídas
    for dano in bola1.verificar_saidas() + bola2.verificar_saidas() + bola3.verificar_saidas():
        vidas -= dano
        pontos += dano * 10

    # Desenhar
    tela.fill(branco)
    bola1.desenhar(tela)
    bola2.desenhar(tela)
    bola3.desenhar(tela)
    pygame.display.flip()

    teclas = pygame.key.get_pressed()
    if teclas[K_a] or teclas[K_LEFT]:
        pos_azul_x -= velocidade_azul
    if teclas[K_d] or teclas[K_RIGHT]:
        pos_azul_x += velocidade_azul

pygame.quit()
sys.exit()