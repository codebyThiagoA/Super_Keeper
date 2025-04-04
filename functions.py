import pygame
from objetos import TAMANHOS_FONTES, POSICOES_ESTATISTICAS, TELA, LARGURA, ALTURA, contadores, posicoes_coracoes
from botao import botao_jogar_rect, botao_sair_rect, botao_reiniciar_rect, botao_sair_gameover_rect
from designs import fundo_inicial, fundo_jogo, fundo_gameover, botao_jogar, botao_sair, botao_reiniciar, coracao, coracao_cinza
import time


def carregar_imagem(caminho, escala=None):
    imagem = pygame.image.load(caminho)
    if escala:
        return pygame.transform.scale(imagem, escala)
    return imagem

def tela_gameover(bola1, bola2, bola3, score, tempo):
    """Tela de Game Over com estatísticas personalizáveis"""
    rodando = True
    fonte_total_bolas = pygame.font.Font(None, TAMANHOS_FONTES['total_bolas'])
    fonte_tempo_score = pygame.font.Font(None, TAMANHOS_FONTES['tempo/score'])
    fonte_bolas = pygame.font.Font(None, TAMANHOS_FONTES['bolas'])

    # Exibe o tempo em segundos (ex.: "125 s")
    tempo_formatado = f"{tempo} s"
    # Calcula o total de bolas coletadas
    total_bolas = bola1 + bola2 + bola3

    elementos = [ 
        {   # Bolas tipo 1
            'texto': f"{bola1}",
            'fonte': fonte_bolas,
            'pos': POSICOES_ESTATISTICAS['bola1'],
            'cor': (255, 255, 255)
        },
        {   # Bolas tipo 2
            'texto': f"{bola2}",
            'fonte': fonte_bolas,
            'pos': POSICOES_ESTATISTICAS['bola2'],
            'cor': (255, 255, 255)
        },
        {   # Bolas tipo 3
            'texto': f"{bola3}",
            'fonte': fonte_bolas,
            'pos': POSICOES_ESTATISTICAS['bola3'],
            'cor': (255, 255, 255)
        },
        {   # Pontuação
            'texto': f"{score}",
            'fonte': fonte_tempo_score,
            'pos': POSICOES_ESTATISTICAS['score'],
            'cor': (255, 255, 255)
        },
        {   # Tempo
            'texto': f"{tempo_formatado}",
            'fonte': fonte_tempo_score,
            'pos': POSICOES_ESTATISTICAS['tempo'],
            'cor': (255, 255, 255)
        },
        {   # Total de bolas
            'texto': f"{total_bolas}",
            'fonte': fonte_total_bolas,
            'pos': POSICOES_ESTATISTICAS['total'],
            'cor': (255, 255, 255)
        }
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

        TELA.blit(fundo_gameover, (0,0))
        
        # Renderiza todos os elementos de texto
        for elemento in elementos:
            texto = elemento['fonte'].render(elemento['texto'], True, elemento['cor'])
            retangulo = texto.get_rect(center=elemento['pos'])
            TELA.blit(texto, retangulo)
        
        # Botões
        TELA.blit(botao_reiniciar, botao_reiniciar_rect)
        TELA.blit(botao_sair, botao_sair_gameover_rect)
        
        pygame.display.flip()

def tela_jogo():
    """Tela principal do jogo"""
    global coracoes_visiveis
    coracoes_visiveis = [True] * 5
    inicio_tempo = time.time()
    estado = {
        'pontos': 0,
        'bola1': 0,
        'bola2': 0,
        'bola3': 0,
        'vidas': 5
    }

    while True:
        tempo_atual = int(time.time() - inicio_tempo)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            if evento.type == pygame.KEYDOWN:
                '''if evento.key == pygame.K_SPACE and estado['vidas'] > 0:
                    estado['vidas'] -= 1
                    coracoes_visiveis[estado['vidas']] = False
                    estado['bola1'] += 1'''

        if estado['vidas'] == 0:
            tela_gameover(estado['bola1'], estado['bola2'], estado['bola3'], estado['pontos'], tempo_atual)
            return

        # Atualiza a tela
        TELA.blit(fundo_jogo, (0,0))
        
        # Desenha corações
        for i, pos in enumerate(posicoes_coracoes):
            TELA.blit(coracao if coracoes_visiveis[i] else coracao_cinza, pos)
        
        # Desenha contadores
        TELA.blit(contadores['timer_img'], contadores['posicoes']['timer'])
        TELA.blit(contadores['bola1_img'], contadores['posicoes']['bola1'])
        TELA.blit(contadores['bola2_img'], contadores['posicoes']['bola2'])
        TELA.blit(contadores['bola3_img'], contadores['posicoes']['bola3'])
        
        # Textos dinâmicos
        fonte = pygame.font.Font(None, 36)
        textos = {
            'tempo': fonte.render(f"{tempo_atual}", True, (255, 255, 255)),
            'score': fonte.render(f"Score: {estado['pontos']}", True, (255, 255, 255)),
            'bola1': fonte.render(f"{estado['bola1']}", True, (255, 255, 255)),
            'bola2': fonte.render(f"{estado['bola2']}", True, (255, 255, 255)),
            'bola3': fonte.render(f"{estado['bola3']}", True, (255, 255, 255))
        }
        
        # Posiciona textos
        TELA.blit(textos['tempo'], (contadores['posicoes']['timer'][0] + 50, contadores['posicoes']['timer'][1] + 10))
        TELA.blit(textos['score'], (contadores['posicoes']['score'][0], contadores['posicoes']['score'][1]))
        TELA.blit(textos['bola1'], (contadores['posicoes']['bola1'][0] + 50, contadores['posicoes']['bola1'][1] + 10))
        TELA.blit(textos['bola2'], (contadores['posicoes']['bola2'][0] + 50, contadores['posicoes']['bola2'][1] + 10))
        TELA.blit(textos['bola3'], (contadores['posicoes']['bola3'][0] + 50, contadores['posicoes']['bola3'][1] + 10))
        
        pygame.display.flip()

def tela_inicial():
    """Tela inicial do jogo"""
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
        
        TELA.blit(fundo_inicial, (0,0))
        TELA.blit(botao_jogar, botao_jogar_rect)
        TELA.blit(botao_sair, botao_sair_rect)
        pygame.display.flip()

if __name__ == "__main__":
    tela_inicial()

