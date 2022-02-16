import pygame


class Load_a_tournament:

    def __init__(self, y, x, id_tournament):

        # var about the player
        self.img = pygame.image.load('assets/button/load.png')
        self.img = pygame.transform.scale(self.img, (150, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id_tournament = id_tournament
