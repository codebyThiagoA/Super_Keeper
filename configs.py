import pygame


# Configurações da tela
LARGURA, ALTURA = 800, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Super Keeper")
clock = pygame.time.Clock()

# Constantes
POSICOES_ESTATISTICAS = {
    'bola1': (250, 480), 'bola2': (379, 480), 'bola3': (505, 480), 'coracao': (615, 480), 
    'tempo': (370, 400), 'score': (590, 400), 'total': (465, 300)
}
TAMANHOS_FONTES = {'total_bolas': 70, 'tempo/score': 60, 'bolas': 45, 'coracao': 45}
posicoes_coracoes = [(650, 105), (675, 105), (700, 105), (725, 105), (750, 105)]
contadores = {
    'posicoes': {
        'bola1': (10, 15), 'bola2': (10, 60), 'bola3': (10, 105),
        'score': (665, 70), 'timer': (665, 15)
    }
}
