#  o goleiro e item são tuplas contendo um sprite (item[0]) e um objeto (item[1]) que possui atributos como posição (x, y) e sprite_id.

def collide(self, colididos, goleiro_player, goleiro, item):
    if goleiro[0].get_rect(topleft=(goleiro_player.x, goleiro_player.y)).colliderect(item[0].get_rect(topleft=(item[1].x, item[1].y))):
        itens = [self.bola_1, self.bola_2, self.bola_3]
        itens[item[1].sprite_id] += 1
        colididos.append(item)

    return colididos
