import pygame
import sys
import random

pygame.init()

altura, largura = 700,800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sistema de Bolas")

branco = (255, 255, 255)
clock = pygame.time.Clock()
def collide(self, goalkeeper, goleiro, item, ):
    if goalkeeper_rect.colliderect(item):
        itens = [self.bola1, self.bola2, self.bola3]
        if item=="bola1":
            qtd_bola1+=1
            pontos+=bola1["pontos"]
        elif item == "bola2":
            qtd_bola2 += 1
            pontos += bola2["pontos"]
        elif item == "bola3":
            qtd_bola3 += 1
            pontos += bola3["pontos"]
    elif item_rect.top > goalkeeper_rect.bottom:
        if item=="bola1":
            vida-=bola1["dano"]
        elif item == "bola2":
            vida -= bola2["dano"]
        elif item == "bola3":
            vida -= bola3["dano"]


class Goalkeeper: #Classe do goleiro

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
            
class BolaBase:
    def __init__(self, velocidade_base, dano, intervalo_base, imagem_path):
        self.v_base = velocidade_base
        self.intervalo_base = intervalo_base
        self.dano = dano
        self.timer = 0
        self.bolas = []

        # Carrega imagem ou cria uma bola colorida se não encontrar
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

# Classes específicas de bolas
class Bola1(BolaBase):
    def __init__(self):
        super().__init__(
            velocidade_base=1.25, 
            dano=1, 
            intervalo_base=254,  # 60 FPS * 3 segundos = 180 frames
            imagem_path="Bola1.png"
        )

class Bola2(BolaBase):
    def __init__(self):
        super().__init__(
            velocidade_base=(2.3), 
            dano=2, 
            intervalo_base=567,  # 60 FPS * 7.5 segundos = 450 frames
            imagem_path="Bola2.png"
        )

class Bola3(BolaBase):
    def __init__(self):
        super().__init__(
            velocidade_base=3.4, 
            dano=3, 
            intervalo_base=823,  # 60 FPS * 10 segundos = 600 frames
            imagem_path="Bola3.png"
        )
# Instanciar bolas
bola1 = Bola1()
bola2 = Bola2()
bola3 = Bola3()
item=[bola1,bola2,bola3]
goalkeeper=Goalkeeper()
pontos = 0
rodando = True
item=(bola1, bola2, bola3)
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualização
    bola1.atualizar(pontos)
    bola2.atualizar(pontos)
    bola3.atualizar(pontos)

    # Verificar saídas (aumenta pontos quando bolas saem)
    for _ in bola1.verificar_saidas() + bola2.verificar_saidas() + bola3.verificar_saidas():
        pontos += 1

    # Desenhar
    tela.fill(branco)
    bola1.desenhar(tela)
    bola2.desenhar(tela)
    bola3.desenhar(tela)
    collide(self,  goalkeeper,  item,)
    # Mostrar pontos
    fonte = pygame.font.SysFont(None, 36)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (0, 0, 0))
    tela.blit(texto_pontos, (10, 10))
    
    pygame.display.flip()

pygame.quit()
sys.exit()