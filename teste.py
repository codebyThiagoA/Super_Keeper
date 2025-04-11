import pygame
import time
from objetos import *
from configs import *
from designs import *  
from audio import *  
from functions import *

# Inicializa pygame e configura o relógio
pygame.init()
clock = pygame.time.Clock()
coracoes_visiveis = [True] * 5  

# Estado inicial do jogo
estado = {'pontos': 0, 'bola1': 0, 'bola2': 0, 'bola3': 0, 'coracao': 0, 'vidas': 5}
inicio_tempo = time.time()

# Instancia as bolas e objetos do jogo
bola1 = BolaBase(1.75, 1, 254, "Bola1.png")
bola2 = BolaBase(2.3, 2, 567, "Bola2.png")
bola3 = BolaBase(2.8, 3, 823, "Bola3.png")
bolas = [bola1, bola2, bola3]
recuperar_coracao = RecuperarCoracao(2.0, 1000, "designs/recuperar_coracao.png")
goalkeeper = Goalkeeper(375, 600, 8, 100, "Goleiro_1.png")

# TELA INICIAL
som_tela_inicial.play()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_jogar_rect.collidepoint(evento.pos):
                pygame.mixer.stop()
                break
            elif botao_sair_rect.collidepoint(evento.pos):
                pygame.quit()
                exit()
    TELA.blit(fundo_inicial, (0, 0))
    TELA.blit(botao_jogar, botao_jogar_rect)
    TELA.blit(botao_sair, botao_sair_rect)
    pygame.display.update()

# TELA INTERMEDIÁRIA
pygame.mixer.music.set_volume(0.67)
tocar_som_estadio()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            break
    TELA.blit(fundo_intermediario, (0, 0))
    pygame.display.update()

# LOOP PRINCIPAL DO JOGO
while True:
    tempo_atual = int(time.time() - inicio_tempo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            parar_som_estadio()
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    goalkeeper.move(keys, LARGURA)

    dano_total = 0
    for bola in bolas:
        for b in bola.bolas[:]:
            if goalkeeper.check_collision(b["rect"]):
                tocar_som_defesa()
                estado['pontos'] += bola.dano * 10
                bola.bolas.remove(b)
                estado[f'bola{bola.dano}'] += 1
        dano_total += bola.atualizar(estado['pontos'])

    recuperar_coracao.atualizar(estado['pontos'])
    for c in recuperar_coracao.coracoes[:]:
        if goalkeeper.check_collision(c["rect"]):
            if estado['vidas'] < 5:
                estado['vidas'] += 1
                coracoes_visiveis[estado['vidas'] - 1] = True
                estado['coracao'] += 1
                pygame.mixer.Sound('audio/som_ganhar vida.wav').play()
            recuperar_coracao.coracoes.remove(c)

    if dano_total > 0:
        tocar_som_perda_vida()

    estado['vidas'] -= dano_total
    if estado['vidas'] <= 0:
        tocar_som_derrota()
        parar_som_estadio()
        mostrar_tela_gameover(estado, tempo_atual)  # <-- functions.py
        break

    for i in range(5):
        coracoes_visiveis[i] = i < estado['vidas']

    TELA.blit(fundo_jogo, (0, 0))
    for bola in bolas:
        bola.desenhar(TELA)
    recuperar_coracao.desenhar(TELA)
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

    pygame.display.update()
    clock.tick(60)
