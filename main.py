import pygame
import math
from game import Game

pygame.init()


#fenetre
pygame.display.set_caption('Checkmate Tournament')
screen = pygame.display.set_mode((1280, 720))

#load bg
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1280, 720))

# * HH import des boutons du menu
play_button = pygame.image.load('assets/button/new_game.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4) - 50
play_button_rect.y = math.ceil(screen.get_height() / 2)

load_button = pygame.image.load('assets/button/load_game.png')
load_button_rect = play_button.get_rect()
load_button_rect.x = math.ceil(screen.get_width() / 4) * 2 + 50
load_button_rect.y = math.ceil(screen.get_height() / 2)

# * HH Charge la Favicon
icon_32x32 = pygame.image.load("assets/favicon.png").convert_alpha()
# * HH Applique la Favicon
pygame.display.set_icon(icon_32x32)

running = True
game = Game(screen)

while running:

    if game.is_launch:
        game.update(screen)
    else:
        # app les image
        screen.blit(background, (0, 0))
        screen.blit(play_button, play_button_rect)
        screen.blit(load_button, load_button_rect)
    

    #update le screen
    pygame.display.flip()

    #if leave
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("le jeu ce ferme")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # * HH verifier que lors du click de la souris, on est bien sur les boutons
            if play_button_rect.collidepoint(event.pos):
                game.is_launch = True

            if load_button_rect.collidepoint(event.pos):
                print('load')