import pygame


class Add_player:
    """Object who will be the add button in the process of creating a player"""

    def __init__(self, y, x, show, id_player):
        """ Method to mannage the button add player

        Args:
            y (int): the y position of the button
            x (int): the x position of the button
            show (bool): a bool to say if we have to show the button or hide it
            id_player (int): this assign a player's id to this button
        """

        # var about the player
        self.img = pygame.image.load('assets/button/add_player.png')
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.show = show
        self.id_player = id_player
