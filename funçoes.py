import pygame as pg
from random import randint


def spawn_bola(frame_count):
    width, height = pg.display.get_window_size()
    
    # Gerando posição X aleatória dentro de um intervalo específico
    spawn_x = randint(width // 6, int(5 * width // 6))
    
    # Gerando posição Y aleatória dentro do topo da tela
    spawn_y = randint(0, height // 16)
    
    # Escolher um tipo de bola aleatório entre 0 e 2
    tipo_bola = randint(0, 2)
    
    obj = Bola(spawn_x, spawn_y, tipo_bola, frame_count)
    
    return [sprite_sheet[obj.sprite_id], obj]

def dificuldade_game(frame_count, dificuldade, onscreen):
    
    dificuldade = int((1 + frame_count / 360) ** 0.4) + 1
    speed_game = int((4 + frame_count / 300) ** 0.5)
    if frame_count % int(60 / (dificuldade / 1.5)) == 0 and len(onscreen) < 1 + dificuldade * 1.1:
        nova_bola = spawn_bola(frame_count)
        onscreen.append(nova_bola)

    return frame_count, dificuldade, onscreen, speed_game
