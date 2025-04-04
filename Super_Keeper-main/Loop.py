# Loop principal corrigido
rodando = True
while vida > 0 and rodando:
    clock.tick(60)
    
    # Eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    # Movimento
    keys = pg.key.get_pressed()
    goalkeeper.move(keys, largura)

    # Atualização das bolas e colisões
    dano_total = 0
    for bola in bolas:
        # Verifica colisões primeiro
        for b in bola.bolas[:]:
            if goalkeeper.check_collision(b["rect"]):
                pontos += bola.dano * 10
                bola.bolas.remove(b)
                if b=="bola1":
                    qtd_bola1+=1
                elif b=="bola2":
                    qtd_bola2+=1
                elif b=="bola3":
                    qtd_bola3+=1
        
        # Atualiza posições e acumula dano
        dano_total += bola.atualizar(pontos)
    
    # Aplica dano no final do frame
    vida -= dano_total

    # Renderização
    tela.fill(branco)
    for bola in bolas:
        bola.desenhar(tela)
    
    # Desenha goleiro
    pg.draw.rect(tela, (0, 0, 255), pg.Rect(goalkeeper.x, goalkeeper.y, goalkeeper.width, 100))
    
    # UI
    fonte = pg.font.SysFont(None, 36)
    texto = fonte.render(f"Pontos: {pontos}  Vida: {vida}", True, (0, 0, 0))
    tela.blit(texto, (10, 10))
    
    pg.display.flip()
