import pygame as pg
from sprite_sheet import sprites_player












esc=False

while running:

        screen.blit(background_game, (0,0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
                exit()
        


        if not esc:
             

            removidos = []
            colididos = []
            for item in onscreen:
                colisoes = pygame.sprite.spritecollide(goleiro, grupo_bolas, True)
                pontuacao += len(colisoes)