import pygame


class Load_a_tournament:
    """Object to manage the load button of a tournament
    """

    def __init__(self, y, x, id_tournament):
        """Method to manage the button load of a tournament

        Args:
            y (int): position Y of the button
            x (int): position X of the button
            id_tournament (int): id of the tournament 
        """

        self.img = pygame.image.load('assets/button/load.png')
        self.img = pygame.transform.scale(self.img, (150, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id_tournament = id_tournament
