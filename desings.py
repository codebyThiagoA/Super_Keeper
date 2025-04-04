from functions import carregar_imagem
from objetos import LARGURA, ALTURA

fundo_inicial = carregar_imagem("designs/Tela_inicial.png", (LARGURA, ALTURA))
fundo_jogo = carregar_imagem("designs/Campo.png", (LARGURA, ALTURA))
fundo_gameover = carregar_imagem("designs/Gameover.png", (LARGURA, ALTURA))
botao_jogar = carregar_imagem("designs/Botao_jogar.png")
botao_sair = carregar_imagem("designs/Botao_sair.png")
botao_reiniciar = carregar_imagem("designs/Botao_jogar_novamente.png")
coracao = carregar_imagem("designs/Coracao.png", (30, 30))
coracao_cinza = carregar_imagem("designs/Coracao_perdido.png", (30, 30))
contadores = {
    'timer_img': carregar_imagem("designs/Relogio.png", (100, 40)),
    'bola1_img': carregar_imagem("designs/Contador_bola1.png", (100, 40)),
    'bola2_img': carregar_imagem("designs/Contador_bola2.png", (100, 40)),
    'bola3_img': carregar_imagem("designs/Contador_bola3.png", (100, 40)),
} 