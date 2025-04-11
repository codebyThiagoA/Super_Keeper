import pygame
from configs import LARGURA, ALTURA, TELA, POSICOES_ESTATISTICAS, TAMANHOS_FONTES, posicoes_coracoes, contadores


def carregar_imagem(caminho, escala=None):
    imagem = pygame.image.load(caminho).convert_alpha()
    if escala:
        return pygame.transform.scale(imagem, escala)
    return imagem

fundo_inicial = carregar_imagem("designs/Tela_inicial.png", (LARGURA, ALTURA))
fundo_jogo = carregar_imagem("designs/Campo.png", (LARGURA, ALTURA))
fundo_gameover = carregar_imagem("designs/gameover.png", (LARGURA, ALTURA))
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