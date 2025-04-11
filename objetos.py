from designs import botao_jogar, botao_sair, botao_reiniciar
from configs import LARGURA, ALTURA

botao_jogar_rect = botao_jogar.get_rect(topleft=(20, 280))
botao_sair_rect = botao_sair.get_rect(topleft=(20, 410))
botao_reiniciar_rect = botao_reiniciar.get_rect(center=(LARGURA // 2, ALTURA // 2 + 200))
botao_sair_gameover_rect = botao_sair.get_rect(center=(LARGURA // 2, ALTURA // 2 + 270))