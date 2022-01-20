import pygame
import math

#create class game
class Game:

    def __init__(self, screen):
        self.is_launch = False
        self.players = []
        self.screen = screen
        self.background = pygame.image.load('assets/bg-2.jpeg')
        self.background = pygame.transform.scale(self.background, (1280, 720))
    
    def update(self, screen):
        print("coucou")
        screen.blit(self.background, (0, 0))