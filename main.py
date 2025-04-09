# coding: utf-8
import pygame
import pygame as pg
import time
import random
import sys

pygame.init()

# Configurações da tela
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

# Carregamento de imagens
def carregar_imagem(caminho, escala=None):
    imagem = pygame.image.load(caminho).convert_alpha()
    if escala:
        return pygame.transform.scale(imagem, escala)
    return imagem

som_tela_inicial = pygame.mixer.Sound('audio/som_tela_inicial.wav')
som_estadio = 'audio/som_estadio.mp3'
som_perda_vida = pygame.mixer.Sound('audio/som_perda_vida.wav')
som_defesa = pygame.mixer.Sound('audio/som_defesa.wav')
som_derrota = pygame.mixer.Sound('audio/som_derrota.wav')


def tocar_som_tela_inicial():
    som_tela_inicial.play()
def tocar_som_estadio():
    pygame.mixer.music.load(som_estadio)
    pygame.mixer.music.play(-1)  # Loop infinito
def parar_som_estadio():
    pygame.mixer.music.stop()
def tocar_som_perda_vida():
    som_perda_vida.play()
def tocar_som_defesa():
    som_defesa.play()
def tocar_som_derrota():
    som_derrota.play()

    
fundo_inicial = carregar_imagem("designs/Tela_inicial.png", (LARGURA, ALTURA))
fundo_jogo = carregar_imagem("designs/Campo.png", (LARGURA, ALTURA))
fundo_gameover = carregar_imagem("designs/Gameover.png", (LARGURA, ALTURA))
botao_jogar = carregar_imagem("designs/Botao_jogar.png")
botao_sair = carregar_imagem("designs/Botao_sair.png")
botao_reiniciar = carregar_imagem("designs/Botao_jogar_novamente.png")
coracao = carregar_imagem("designs/Coracao.png", (30, 30))
coracao_cinza = carregar_imagem("designs/Coracao_perdido.png", (30, 30))
contadores.update({
    'timer_img': carregar_imagem("designs/Relogio.png", (100, 40)),
    'bola1_img': carregar_imagem("designs/Contador_bola1.png", (100, 40)),
    'bola2_img': carregar_imagem("designs/Contador_bola2.png", (100, 40)),
    'bola3_img': carregar_imagem("designs/Contador_bola3.png", (100, 40)),
})

# Retângulos dos botões
botao_jogar_rect = botao_jogar.get_rect(topleft=(20, 280))
botao_sair_rect = botao_sair.get_rect(topleft=(20, 410))
botao_reiniciar_rect = botao_reiniciar.get_rect(center=(LARGURA // 2, ALTURA // 2 + 200))
botao_sair_gameover_rect = botao_sair.get_rect(center=(LARGURA // 2, ALTURA // 2 + 270))

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

# Funções de tela
def tela_gameover(bola1, bola2, bola3, score, tempo):
    rodando = True
    fonte_total_bolas = pygame.font.Font(None, TAMANHOS_FONTES['total_bolas'])
    fonte_tempo_score = pygame.font.Font(None, TAMANHOS_FONTES['tempo/score'])
    fonte_bolas = pygame.font.Font(None, TAMANHOS_FONTES['bolas'])
    tempo_formatado = f"{tempo} s"
    total_bolas = bola1 + bola2 + bola3

    elementos = [
        {'texto': f"{bola1}", 'fonte': fonte_bolas, 'pos': POSICOES_ESTATISTICAS['bola1'], 'cor': (255, 255, 255)},
        {'texto': f"{bola2}", 'fonte': fonte_bolas, 'pos': POSICOES_ESTATISTICAS['bola2'], 'cor': (255, 255, 255)},
        {'texto': f"{bola3}", 'fonte': fonte_bolas, 'pos': POSICOES_ESTATISTICAS['bola3'], 'cor': (255, 255, 255)},
        {'texto': f"{score}", 'fonte': fonte_tempo_score, 'pos': POSICOES_ESTATISTICAS['score'], 'cor': (255, 255, 255)},
        {'texto': f"{tempo_formatado}", 'fonte': fonte_tempo_score, 'pos': POSICOES_ESTATISTICAS['tempo'], 'cor': (255, 255, 255)},
        {'texto': f"{total_bolas}", 'fonte': fonte_total_bolas, 'pos': POSICOES_ESTATISTICAS['total'], 'cor': (255, 255, 255)}
    ]
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar_rect.collidepoint(evento.pos):
                    tela_jogo()
                if botao_sair_gameover_rect.collidepoint(evento.pos):
                    pygame.quit()
                    return
        TELA.blit(fundo_gameover, (0, 0))
        for elemento in elementos:
            texto = elemento['fonte'].render(elemento['texto'], True, elemento['cor'])
            retangulo = texto.get_rect(center=elemento['pos'])
            TELA.blit(texto, retangulo)
        TELA.blit(botao_reiniciar, botao_reiniciar_rect)
        TELA.blit(botao_sair, botao_sair_gameover_rect)
        pygame.display.flip()

def tela_jogo():
    global coracoes_visiveis
    coracoes_visiveis = [True] * 5
    inicio_tempo = time.time()
    estado = {'pontos': 0, 'bola1': 0, 'bola2': 0, 'bola3': 0, 'vidas': 5}
    bola1 = BolaBase(1.75, 1, 254, "Bola1.png")
    bola2 = BolaBase(2.3, 2, 567, "Bola2.png")
    bola3 = BolaBase(2.8, 3, 823, "Bola3.png")
    bolas = [bola1, bola2, bola3]
    goalkeeper = Goalkeeper(LARGURA // 2 - 50, 600, 8, 100, "Goleiro_1.png")

    pygame.mixer.music.set_volume(0.47) 
    tocar_som_estadio()
    while True:
        tempo_atual = int(time.time() - inicio_tempo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                parar_som_estadio()
                return

        keys = pygame.key.get_pressed()
        goalkeeper.move(keys, LARGURA)

        dano_total = 0
        for bola in bolas:
            for b in bola.bolas[:]:
                if goalkeeper.check_collision(b["rect"]):
                    tocar_som_defesa()  
                    estado['pontos'] += bola.dano * 10
                    bola.bolas.remove(b)
                    if bola == bola1:
                        estado['bola1'] += 1
                    elif bola == bola2:
                        estado['bola2'] += 1
                    elif bola == bola3:
                        estado['bola3'] += 1
            dano_total += bola.atualizar(estado['pontos'])

        if dano_total > 0:
            tocar_som_perda_vida()  # Tocar som de perda de vida

        estado['vidas'] -= dano_total
        if estado['vidas'] <= 0:
            tocar_som_derrota()  # Tocar som de derrota
            parar_som_estadio()  # Parar o som do estádio ao sair da tela de jogo
            tela_gameover(estado['bola1'], estado['bola2'], estado['bola3'], estado['pontos'], tempo_atual)
            return
        for i in range(5):
            coracoes_visiveis[i] = i < estado['vidas']

        TELA.blit(fundo_jogo, (0, 0))
        for bola in bolas:
            bola.desenhar(TELA)
        TELA.blit(goalkeeper.img, (goalkeeper.x, goalkeeper.y))
        for i, pos in enumerate(posicoes_coracoes):
            TELA.blit(coracao if coracoes_visiveis[i] else coracao_cinza, pos)
        TELA.blit(contadores['timer_img'], contadores['posicoes']['timer'])
        TELA.blit(contadores['bola1_img'], contadores['posicoes']['bola1'])
        TELA.blit(contadores['bola2_img'], contadores['posicoes']['bola2'])
        TELA.blit(contadores['bola3_img'], contadores['posicoes']['bola3'])

        fonte = pygame.font.Font(None, 36)
        textos = {
            'tempo': fonte.render(f"{tempo_atual}", True, (255, 255, 255)),
            'score': fonte.render(f"Score: {estado['pontos']}", True, (255, 255, 255)),
            'bola1': fonte.render(f"{estado['bola1']}", True, (255, 255, 255)),
            'bola2': fonte.render(f"{estado['bola2']}", True, (255, 255, 255)),
            'bola3': fonte.render(f"{estado['bola3']}", True, (255, 255, 255))
        }
        TELA.blit(textos['tempo'], (contadores['posicoes']['timer'][0] + 50, contadores['posicoes']['timer'][1] + 10))
        TELA.blit(textos['score'], (contadores['posicoes']['score'][0], contadores['posicoes']['score'][1]))
        TELA.blit(textos['bola1'], (contadores['posicoes']['bola1'][0] + 50, contadores['posicoes']['bola1'][1] + 10))
        TELA.blit(textos['bola2'], (contadores['posicoes']['bola2'][0] + 50, contadores['posicoes']['bola2'][1] + 10))
        TELA.blit(textos['bola3'], (contadores['posicoes']['bola3'][0] + 50, contadores['posicoes']['bola3'][1] + 10))

        pygame.display.flip()
        clock.tick(60)

def tela_inicial():
    som_tocou = False  # Variável para controlar se o som já foi tocado
    while True:
        for evento in pygame.event.get():
            if not som_tocou:
                tocar_som_tela_inicial()  # Toca o som da tela inicial apenas uma vez
                som_tocou = True
            if evento.type == pygame.QUIT:
                pygame.mixer.stop()  # Para todos os sons
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar_rect.collidepoint(evento.pos):
                    pygame.mixer.stop()  # Para o som ao iniciar o jogo
                    tela_jogo()
                if botao_sair_rect.collidepoint(evento.pos):
                    pygame.mixer.stop()  # Para o som ao sair
                    pygame.quit()
                    return
        TELA.blit(fundo_inicial, (0, 0))
        TELA.blit(botao_jogar, botao_jogar_rect)
        TELA.blit(botao_sair, botao_sair_rect)
        pygame.display.flip()

if __name__ == "__main__":
    tela_inicial()