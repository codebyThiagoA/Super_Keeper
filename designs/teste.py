import pygame
import os

# Inicializar o pygame
pygame.init()

# Definir dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Keeper")

# Definir o diretório base como o local do script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtém o caminho do script atual
os.chdir(script_dir)  # Define esse diretório como o diretório de trabalho

# Caminho da imagem
image_path = os.path.join(script_dir, "campo.png")

# Verificar se a imagem existe antes de carregar
if not os.path.exists(image_path):
    print(f"Erro: O arquivo '{image_path}' não foi encontrado.")
    pygame.quit()
    exit()

# Carregar a imagem do fundo
background = pygame.image.load(image_path).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Controlador de FPS
clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenhar a imagem de fundo
    screen.blit(background, (0, 0))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS
    clock.tick(60)

# Fechar o pygame
pygame.quit()
