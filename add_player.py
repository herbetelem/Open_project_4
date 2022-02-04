import pygame

# create class add_player


class Add_player:

    def __init__(self, y, x, show, id_player):
        # var about the player
        self.img = pygame.image.load('assets/button/add_player.png')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.show = show
        self.id_player = id_player
