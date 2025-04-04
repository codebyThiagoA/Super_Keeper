import pygame as pg
import sys
import random

pg.init()

# Configurações da tela
altura, largura = 700, 800
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Sistema de Bolas")

branco = (255, 255, 255)
clock = pg.time.Clock()

# Classe base das bolas (modificada para controle de dano)
class BolaBase:
    def __init__(self, velocidade_base, dano, intervalo_base, imagem_path, ):
        self.v_base = velocidade_base
        self.intervalo_base = intervalo_base
        self.dano = dano
        self.timer = 0
        self.bolas = []
        
        self.img = pg.image.load(imagem_path).convert_alpha()
        self.img = pg.transform.scale(self.img, (60, 60))
        
    def velocidade_atual(self, pontos):
        return self.v_base + (self.v_base * pontos / 150)

    def intervalo_atual(self, pontos):
        return max(10, int(self.intervalo_base - (pontos / 10)))

    def spawn(self):
        rect = self.img.get_rect()
        rect.x = random.randint(0, largura - rect.width)
        rect.y = -rect.height
        return {"img": self.img, "rect": rect}

    def atualizar(self, pontos):
        self.timer += 1
        dano_causado = 0
        # Spawn de novas bolas
        if self.timer >= self.intervalo_atual(pontos):
            self.bolas.append(self.spawn())
            self.timer = 0
        
        # Atualiza posição e verifica saída da tela
        novas_bolas = []
        for b in self.bolas:
            b["rect"].y += self.velocidade_atual(pontos)
            
            # Mantém apenas as bolas que ainda estão visíveis
            if b["rect"].top <= altura:
                novas_bolas.append(b)
            else:
                dano_causado += self.dano  # Acumula dano
                
        self.bolas = novas_bolas
        return dano_causado

    def desenhar(self, tela):
        for b in self.bolas:
            tela.blit(b["img"], b["rect"])

# Classe do goleiro mantida
class Goalkeeper:
    def __init__(self, posicao_x, posicao_y, speed, width):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.speed = speed
        self.width = width
        self.lives = 4

    @property
    def x(self):
        return self.posicao_x

    @property
    def y(self):
        return self.posicao_y

    def move(self, keys, screen_width):
        if keys[pg.K_RIGHT] and self.x < screen_width - self.width:
            self.posicao_x += self.speed
        if keys[pg.K_LEFT] and self.x > 0:
            self.posicao_x -= self.speed

    def check_collision(self, ball_rect):
        goalkeeper_rect = pg.Rect(self.x, self.y, self.width, 100)
        return goalkeeper_rect.colliderect(ball_rect)

# Instâncias e inicialização
bola1 = BolaBase(1.75, 1, 254, "Bola1.png")
bola2 = BolaBase(2.3, 2, 567, "Bola2.png")
bola3 = BolaBase(2.8, 3, 823, "Bola3.png")
bolas = [bola1, bola2, bola3]
goalkeeper = Goalkeeper(largura // 2 - 50, 600, 5, 100)
pontos = 0
vida = 5
qtd_bola1=0
qtd_bola2=0
qtd_bola3=0

# Loop principal corrigido
rodando = True
while vida > 0 and rodando:
    clock.tick(60)
    
    # Eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    # Movimento
    keys = pg.key.get_pressed()
    goalkeeper.move(keys, largura)

    # Atualização das bolas e colisões
    dano_total = 0
    for bola in bolas:
        # Verifica colisões primeiro
        for b in bola.bolas[:]:
            if goalkeeper.check_collision(b["rect"]):
                pontos += bola.dano * 10
                bola.bolas.remove(b)
                if b=="bola1":
                    qtd_bola1+=1
                elif b=="bola2":
                    qtd_bola2+=1
                elif b=="bola3":
                    qtd_bola3+=1
        
        # Atualiza posições e acumula dano
        dano_total += bola.atualizar(pontos)
    
    # Aplica dano no final do frame
    vida -= dano_total

    # Renderização
    tela.fill(branco)
    for bola in bolas:
        bola.desenhar(tela)
    
    # Desenha goleiro
    pg.draw.rect(tela, (0, 0, 255), pg.Rect(goalkeeper.x, goalkeeper.y, goalkeeper.width, 100))
    
    # UI
    fonte = pg.font.SysFont(None, 36)
    texto = fonte.render(f"Pontos: {pontos}  Vida: {vida}", True, (0, 0, 0))
    tela.blit(texto, (10, 10))
    
    pg.display.flip()

pg.quit()
sys.exit()