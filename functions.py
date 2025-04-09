import pygame
import time
import random
from objetos import BolaBase, Goalkeeper
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_UP, K_DOWN
from objetos import carregar_imagem
from objetos import LARGURA, ALTURA, TAMANHOS_FONTES, POSICOES_ESTATISTICAS, posicoes_coracoes, contadores, coracao, coracao_cinza, TELA, clock, fundo_inicial, fundo_jogo, fundo_gameover, botao_jogar, botao_sair, botao_reiniciar, botao_sair_gameover,botao_jogar_rect,botao_reiniciar_rect,botao_sair_rect,botao_sair_gameover_rect

# Inicializa o Pygame
def carregar_imagem(caminho, escala=None):
    imagem = pygame.image.load(caminho).convert_alpha()
    if escala:
        return pygame.transform.scale(imagem, escala)
    return imagem


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

    while True:
        tempo_atual = int(time.time() - inicio_tempo)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        goalkeeper.move(keys, LARGURA)

        dano_total = 0
        for bola in bolas:
            for b in bola.bolas[:]:
                if goalkeeper.check_collision(b["rect"]):
                    estado['pontos'] += bola.dano * 10
                    bola.bolas.remove(b)
                    if bola == bola1:
                        estado['bola1'] += 1
                    elif bola == bola2:
                        estado['bola2'] += 1
                    elif bola == bola3:
                        estado['bola3'] += 1
            dano_total += bola.atualizar(estado['pontos'])

        estado['vidas'] -= dano_total
        if estado['vidas'] <= 0:
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
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar_rect.collidepoint(evento.pos):
                    tela_jogo()
                if botao_sair_rect.collidepoint(evento.pos):
                    pygame.quit()
                    return
        TELA.blit(fundo_inicial, (0, 0))
        TELA.blit(botao_jogar, botao_jogar_rect)
        TELA.blit(botao_sair, botao_sair_rect)
        pygame.display.flip()