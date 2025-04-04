import pygame
import sys
import random

pygame.init()

# Tela
altura, largura = 700, 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sistema de Bolas")

# Cores e clock
branco = (255, 255, 255)
clock = pygame.time.Clock()

# Variáveis globais
vida = 5
pontos = 0
qtd_bola1 = 0
qtd_bola2 = 0
qtd_bola3 = 0

# Classe do goleiro
class Goalkeeper:
    def __init__(self, posicao_x, posicao_y, speed, width):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.speed = speed
        self.width = width
        self.lives = 4

    def get_rect(self):
        return pygame.Rect(self.posicao_x, self.posicao_y, self.width, self.width)

    def move(self, keys, screen_width):
        if keys[pygame.K_RIGHT] and self.posicao_x < screen_width - self.width:
            self.posicao_x += self.speed
        if keys[pygame.K_LEFT] and self.posicao_x > 0:
            self.posicao_x -= self.speed

    def collide(self, bolas, pontos, vida, qtd_bola1, qtd_bola2, qtd_bola3):
        goalkeeper_rect = self.get_rect()
        for bola in bolas:
            for b in bola.bolas[:]:
                item_rect = b["rect"]
                if goalkeeper_rect.colliderect(item_rect):
                    if isinstance(bola, Bola1):
                        qtd_bola1 += 1
                        pontos += 1
                    elif isinstance(bola, Bola2):
                        qtd_bola2 += 1
                        pontos += 2
                    elif isinstance(bola, Bola3):
                        qtd_bola3 += 1
                        pontos += 3
                    bola.bolas.remove(b)
                elif item_rect.top > goalkeeper_rect.bottom:
                    vida -= bola.dano
                    bola.bolas.remove(b)
        return pontos, vida, qtd_bola1, qtd_bola2, qtd_bola3

# Classe base das bolas
class BolaBase:
    def __init__(self, velocidade_base, dano, intervalo_base, imagem_path):
        self.v_base = velocidade_base
        self.intervalo_base = intervalo_base
        self.dano = dano
        self.timer = 0
        self.bolas = []
        try:
            self.img = pygame.image.load(imagem_path).convert_alpha()
            self.img = pygame.transform.scale(self.img, (60, 60))
        except:
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

# Classes específicas das bolas
class Bola1(BolaBase):
    def __init__(self):
        super().__init__(1.25, 1, 254, "Bola1.png")

class Bola2(BolaBase):
    def __init__(self):
        super().__init__(2.3, 2, 567, "Bola2.png")

class Bola3(BolaBase):
    def __init__(self):
        super().__init__(3.4, 3, 823, "Bola3.png")

# Instanciar
bola1 = Bola1()
bola2 = Bola2()
bola3 = Bola3()
bolas = [bola1, bola2, bola3]

goleiro = Goalkeeper(largura // 2 - 50, 600, 5, 100)

# Loop principal
rodando = True
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualizar teclas
    keys = pygame.key.get_pressed()
    goleiro.move(keys, largura)

    # Atualizar bolas
    for bola in bolas:
        bola.atualizar(pontos)

    # Verificar saídas
    for dano in bola1.verificar_saidas() + bola2.verificar_saidas() + bola3.verificar_saidas():
        vida -= dano

    # Colisão
    pontos, vida, qtd_bola1, qtd_bola2, qtd_bola3 = goleiro.collide(
        bolas, pontos, vida, qtd_bola1, qtd_bola2, qtd_bola3
    )

    # Desenho
    tela.fill(branco)
    for bola in bolas:
        bola.desenhar(tela)

    # Goleiro
    pygame.draw.rect(tela, (0, 0, 255), goleiro.get_rect())

    # Texto
    fonte = pygame.font.SysFont(None, 36)
    texto = fonte.render(f"Pontos: {pontos}  Vida: {vida}", True, (0, 0, 0))
    tela.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()