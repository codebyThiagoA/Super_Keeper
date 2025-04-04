import pygame as pg

# Inicialização do Pygame
pg.init()

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pg.display.set_caption("Tela Inicial")

# Classe do Botão
class Botao:
    def __init__(self, caminho_imagem, x, y, escala=1):
        # Carrega e redimensiona a imagem
        self.imagem = pg.image.load(caminho_imagem).convert_alpha()
        largura = self.imagem.get_width()
        altura = self.imagem.get_height()
        self.imagem = pg.transform.scale(
            self.imagem, 
            (int(largura * escala), int(altura * escala)))
        
        # Configura retângulo e posição
        self.retangulo = self.imagem.get_rect()
        self.retangulo.topleft = (x, y)
        self.clicado = False

    def desenhar(self, superficie):
        acao = False
        pos_mouse = pg.mouse.get_pos()
        
        # Verifica colisão e clique
        if self.retangulo.collidepoint(pos_mouse):
            if pg.mouse.get_pressed()[0] and not self.clicado:
                self.clicado = True
                acao = True
                
        # Reseta estado do clique
        if not pg.mouse.get_pressed()[0]:
            self.clicado = False
            
        # Desenha na tela
        superficie.blit(self.imagem, self.retangulo)
        return acao

# Carrega fundo
fundo = pg.image.load("Tela_inicial.jpg").convert()
fundo = pg.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA))

# Cria botões centralizados
botao_jogar = Botao(
    caminho_imagem="botao_jogar.png",
    x=LARGURA_TELA//2 - 100,  # Centralizado horizontalmente
    y=ALTURA_TELA//2,         # 300px do topo (para tela 600px)
    escala=0.5
)

botao_sair = Botao(
    caminho_imagem="botao_sair.png",
    x=LARGURA_TELA//2 - 100,
    y=ALTURA_TELA//2 + 100,  # 400px do topo
    escala=0.5
)

# Loop principal
executando = True
while executando:
    # Desenha fundo
    tela.blit(fundo, (0, 0))
    
    # Desenha botões e verifica ações
    acao_jogar = botao_jogar.desenhar(tela)
    acao_sair = botao_sair.desenhar(tela)
    
    # Lógica dos botões
    if acao_jogar:
        print("Jogo iniciado!")
        # executando = False  # Remova o comentário para fechar a tela
        
    if acao_sair:
        executando = False

    # Eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            executando = False

    # Atualiza display
    pg.display.update()

pg.quit()

