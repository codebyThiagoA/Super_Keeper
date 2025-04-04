import pygame

LARGURA, ALTURA = 800, 700
TELA = pygame.display.set_mode((LARGURA, ALTURA))

POSICOES_ESTATISTICAS = {
    # Cada bola ao lado de seu respectivo ícone
    'bola1': (325, 480),   # bola preta e branca
    'bola2': (455, 480),   # bola azul
    'bola3': (585, 480),   # bola vermelha e amarela
    
    # Score e Tempo próximos aos sublinhados "Tempo __" e "Score __"
    'tempo': (390, 400),
    'score': (570, 400),
    
    # Total de bolas coletadas
    'total': (465, 300)
}

TAMANHOS_FONTES = {
    'total_bolas': 70,
    'tempo/score': 60,
    'bolas': 45
}

posicoes_coracoes = [(650, 105), (675, 105), (700, 105), (725, 105), (750, 105)]

contadores = {'posicoes': {
        'bola1': (10, 15),
        'bola2': (10, 60),
        'bola3': (10, 105),
        'score': (665, 70),
        'timer': (665, 15)
    }
}
