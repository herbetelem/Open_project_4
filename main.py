"""This code will manage the windows and the event for the application """

import math
import pygame

from game import Game

pygame.init()

# windows
pygame.display.set_caption('Checkmate Tournament')
screen = pygame.display.set_mode((1280, 720))

# load bg
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1280, 720))

# create button and rect for first menu
play_button = pygame.image.load('assets/button/new_game.png')
play_button = pygame.transform.scale(play_button, (400, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4) - 50
play_button_rect.y = math.ceil(screen.get_height() / 2)

load_button = pygame.image.load('assets/button/load_game.png')
load_button = pygame.transform.scale(load_button, (400, 100))
load_button_rect = load_button.get_rect()
load_button_rect.x = math.ceil(screen.get_width() / 4) * 2 + 50
load_button_rect.y = math.ceil(screen.get_height() / 2)

# * HH Charge la Favicon
icon_32x32 = pygame.image.load("assets/favicon.png").convert_alpha()
# * HH Applique la Favicon
pygame.display.set_icon(icon_32x32)

# manage the game
running = True
game = Game(screen)

# step for create a tournament
step = {
    "name": "country",
    "country": "town",
    "town": "location",
    "location": "date",
    "date": "time",
    "time": "description",
    "description": "player",
    "player": "end"
}


def manage_step(game):
    """ Method to manage the fifferent stp of the creation of the tournament

    Args:
        game (object): the object pygame of the game
    """

    if game.step == "country":
        tmp_country = game.sql.get_country()
        tmp_country = tmp_country[game.index_location]
        game.tournament.country = tmp_country
    if game.step == "town":
        tmp_town = game.sql.get_town(game.tournament.country)
        tmp_town = tmp_town[game.index_location]
        game.tournament.town = tmp_town
    if game.step == "location":
        tmp_location = game.sql.get_location(game.tournament.town)
        tmp_location = tmp_location[game.index_location]
        game.tournament.location = tmp_location
    if game.step == "date":
        game.tournament.date = f"{game.day.str}/{game.month.str}/{game.year.str}"
    if game.step == "time":
        if game.choice == 1:
            game.tournament.time = "bullet"
        elif game.choice == 2:
            game.tournament.time = "blitz"
        elif game.choice == 3:
            game.tournament.time = "coup rapide"
    if game.step == "player" and len(game.players) == 8:
        game.tournament.players = game.players
        game.step = step[game.step]
        game.index_location = 0
    elif game.step != "player":
        game.step = step[game.step]
        game.index_location = 0


while running:

    if game.is_launch or game.load:
        game.update()
    else:
        # app the image of first menu
        screen.blit(background, (0, 0))
        screen.blit(play_button, play_button_rect)
        screen.blit(load_button, load_button_rect)

    # update the screen
    pygame.display.flip()

    for event in pygame.event.get():
        # if leaving
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            game.sql.connector.close()
            print("le jeu ce ferme")

        # if mouseclick
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # manage the first menu
            if game.step is False:
                if play_button_rect.collidepoint(event.pos):
                    game.is_launch = True
                    game.step = "name"
                if load_button_rect.collidepoint(event.pos):
                    game.load = True

            # Manage the load buttons
            if game.load:
                for button in game.history_button:
                    if button.rect.collidepoint(event.pos):
                        game.match_load = button.id_tournament
                if game.prev_rect.collidepoint(event.pos):
                    game.match_load = False

            # manage the next step of creation of a tournament
            elif game.next_up and game.next_rect.collidepoint(event.pos):
                manage_step(game)
            elif game.next_up is False and game.start_rect.collidepoint(event.pos):
                if game.tournament.created is False:
                    game.set_var_game()
                    game.tournament.created = True

            if game.next_up:
                # manage the selection of the date
                if game.step == "date":
                    if game.day.rect.collidepoint(event.pos):
                        if game.day.str == 31:
                            game.day.str = 1
                        else:
                            game.day.str += 1
                    if game.month.rect.collidepoint(event.pos):
                        if game.month.str == 12:
                            game.month.str = 1
                        else:
                            game.month.str += 1
                    if game.year.rect.collidepoint(event.pos):
                        game.year.str += 1

                # manage the selection of turn
                if game.step == "turn":
                    if game.more_rect.collidepoint(event.pos):
                        if game.tournament.nb_turn < 4:
                            game.tournament.nb_turn += 1
                    if game.less_rect.collidepoint(event.pos):
                        if game.tournament.nb_turn > 1:
                            game.tournament.nb_turn -= 1

                # manage the selection of time
                if game.step == "time":
                    if game.choice_A_rect.collidepoint(event.pos):
                        game.choice = 1
                    if game.choice_B_rect.collidepoint(event.pos):
                        game.choice = 2
                    if game.choice_C_rect.collidepoint(event.pos):
                        game.choice = 3

                # manage the selection of players
                if game.step == "player":
                    for button in game.tmp_players:
                        if button.rect.collidepoint(event.pos):
                            if button.id_player not in game.players and \
                                    len(game.players_search) > 0:
                                game.players.append(button.id_player)
                                game.players_search = ""
                                game.step = "player"

            # if the tournament have been created
            if game.next_up is False:
                if game.game_statut:

                    # if the settings have been selected
                    if game.round.settings:
                        for player in game.round.players:
                            if player.rect.collidepoint(event.pos):
                                for all_player in game.round.players:
                                    all_player.img = game.set_an_image(
                                        'assets/button/editer.png', (150, 50))
                                    all_player.selected = False
                                player.img = game.set_an_image(
                                    'assets/button/editer-check.png', (150, 50))
                                player.selected = True

                        if game.validate_rect.collidepoint(event.pos):
                            game.round.generate_round()
                            game.round.settings = False
                            game.deck_1 = pygame.image.load(
                                'assets/match-no-result.png')
                            game.deck_1 = pygame.transform.scale(
                                game.deck_1, (140, 140))
                            game.deck_2 = pygame.image.load(
                                'assets/match-no-result.png')
                            game.deck_2 = pygame.transform.scale(
                                game.deck_2, (140, 140))
                            game.deck_3 = pygame.image.load(
                                'assets/match-no-result.png')
                            game.deck_3 = pygame.transform.scale(
                                game.deck_3, (140, 140))
                            game.deck_4 = pygame.image.load(
                                'assets/match-no-result.png')
                            game.deck_4 = pygame.transform.scale(
                                game.deck_4, (140, 140))
                    else:
                        #  Manage Game desk 1
                        if game.deck_1_rect.collidepoint(event.pos):
                            game.deck_1 = pygame.image.load(
                                'assets/match-nul.png')
                            game.deck_1 = pygame.transform.scale(
                                game.deck_1, (140, 140))
                            game.round.match[0][2] = 3

                        elif game.area_win_1.collidepoint(event.pos):
                            game.deck_1 = pygame.image.load(
                                'assets/match-win-1.png')
                            game.deck_1 = pygame.transform.scale(
                                game.deck_1, (140, 140))
                            game.round.match[0][2] = 1

                        elif game.area_win_2.collidepoint(event.pos):
                            game.deck_1 = pygame.image.load(
                                'assets/match-win-2.png')
                            game.deck_1 = pygame.transform.scale(
                                game.deck_1, (140, 140))
                            game.round.match[0][2] = 2

                        #  Manage Game desk 2
                        if game.deck_2_rect.collidepoint(event.pos):
                            game.deck_2 = pygame.image.load(
                                'assets/match-nul.png')
                            game.deck_2 = pygame.transform.scale(
                                game.deck_2, (140, 140))
                            game.round.match[1][2] = 3

                        elif game.area_win_3.collidepoint(event.pos):
                            game.deck_2 = pygame.image.load(
                                'assets/match-win-1.png')
                            game.deck_2 = pygame.transform.scale(
                                game.deck_2, (140, 140))
                            game.round.match[1][2] = 1

                        elif game.area_win_4.collidepoint(event.pos):
                            game.deck_2 = pygame.image.load(
                                'assets/match-win-2.png')
                            game.deck_2 = pygame.transform.scale(
                                game.deck_2, (140, 140))
                            game.round.match[1][2] = 2

                        #  Manage Game desk 3
                        if game.deck_3_rect.collidepoint(event.pos):
                            game.deck_3 = pygame.image.load(
                                'assets/match-nul.png')
                            game.deck_3 = pygame.transform.scale(
                                game.deck_3, (140, 140))
                            game.round.match[2][2] = 3

                        elif game.area_win_5.collidepoint(event.pos):
                            game.deck_3 = pygame.image.load(
                                'assets/match-win-1.png')
                            game.deck_3 = pygame.transform.scale(
                                game.deck_3, (140, 140))
                            game.round.match[2][2] = 1

                        elif game.area_win_6.collidepoint(event.pos):
                            game.deck_3 = pygame.image.load(
                                'assets/match-win-2.png')
                            game.deck_3 = pygame.transform.scale(
                                game.deck_3, (140, 140))
                            game.round.match[2][2] = 2

                        #  Manage Game desk 4
                        if game.deck_4_rect.collidepoint(event.pos):
                            game.deck_4 = pygame.image.load(
                                'assets/match-nul.png')
                            game.deck_4 = pygame.transform.scale(
                                game.deck_4, (140, 140))
                            game.round.match[3][2] = 3

                        elif game.area_win_7.collidepoint(event.pos):
                            game.deck_4 = pygame.image.load(
                                'assets/match-win-1.png')
                            game.deck_4 = pygame.transform.scale(
                                game.deck_4, (140, 140))
                            game.round.match[3][2] = 1

                        elif game.area_win_8.collidepoint(event.pos):
                            game.deck_4 = pygame.image.load(
                                'assets/match-win-2.png')
                            game.deck_4 = pygame.transform.scale(
                                game.deck_4, (140, 140))
                            game.round.match[3][2] = 2

                        # Manage Validate
                        if game.validate_rect.collidepoint(event.pos):
                            result = []
                            for match in game.round.match:
                                result.append(match[2])
                            game.round.validate_round(result)
                            if game.round.nb_turn < 7:
                                game.round.generate_round()
                                game.deck_1 = pygame.image.load(
                                    'assets/match-no-result.png')
                                game.deck_1 = pygame.transform.scale(
                                    game.deck_1, (140, 140))
                                game.deck_2 = pygame.image.load(
                                    'assets/match-no-result.png')
                                game.deck_2 = pygame.transform.scale(
                                    game.deck_2, (140, 140))
                                game.deck_3 = pygame.image.load(
                                    'assets/match-no-result.png')
                                game.deck_3 = pygame.transform.scale(
                                    game.deck_3, (140, 140))
                                game.deck_4 = pygame.image.load(
                                    'assets/match-no-result.png')
                                game.deck_4 = pygame.transform.scale(
                                    game.deck_4, (140, 140))
                            else:
                                game.game_statut = False
                        elif game.update_score_rect.collidepoint(event.pos):
                            game.round.settings = True

                # Mannage save
                if game.round.nb_turn == 7 and game.save_rect.collidepoint(event.pos):
                    for player in game.round.players:
                        game.sql.save_score(
                            (player.id, game.tournament.id, player.score))
                    game = Game(screen)

        # if use keyboard
        elif event.type == pygame.KEYDOWN:

            if game.next_up:
                # manage the creation of the name
                if game.step == "name" or game.step == "description" or game.step == "player":
                    letters = {x: pygame.key.key_code(
                        x) for x in "abcdefghijklmnopqrstuvwxyz"}
                    touche = pygame.key.get_pressed()
                    for (l, value) in letters.items():
                        if touche[value]:
                            if game.step == "name":
                                if len(game.tournament.description) < 50:
                                    game.tournament.name = game.tournament.name + \
                                        str(l)
                            elif game.step == "description":
                                if len(game.tournament.description) < 200:
                                    game.tournament.description = game.tournament.description + \
                                        str(l)
                            elif game.step == "player":
                                game.players_search = game.players_search + \
                                    str(l)
                    if event.key == pygame.K_SPACE:
                        if game.step == "name":
                            game.tournament.name = game.tournament.name + " "
                        elif game.step == "description":
                            game.tournament.description = game.tournament.description + " "
                        elif game.step == "player":
                            game.players_search = game.players_search + " "
                    elif event.key == pygame.K_BACKSPACE:
                        if game.step == "name":
                            game.tournament.name = game.tournament.name[:-1]
                        elif game.step == "description":
                            game.tournament.description = game.tournament.description[:-1]
                        elif game.step == "player":
                            game.players_search = game.players_search[:-1]

                if game.step == "country":
                    if event.key == pygame.K_LEFT:
                        game.index_location -= 1
                        if game.index_location < 0:
                            game.index_location = len(
                                game.sql.get_country()) - 1
                    elif event.key == pygame.K_RIGHT:
                        game.index_location += 1
                        if game.index_location >= len(game.sql.get_country()):
                            game.index_location = 0

                if game.step == "town":
                    if event.key == pygame.K_LEFT:
                        game.index_location -= 1
                        if game.index_location < 0:
                            game.index_location = len(
                                game.sql.get_town(game.tournament.country)) - 1
                    elif event.key == pygame.K_RIGHT:
                        game.index_location += 1
                        if game.index_location >= len(game.sql.get_town(game.tournament.country)):
                            game.index_location = 0

                if game.step == "location":
                    if event.key == pygame.K_LEFT:
                        game.index_location -= 1
                        if game.index_location < 0:
                            game.index_location = len(
                                game.sql.get_location(game.tournament.town)) - 1
                    elif event.key == pygame.K_RIGHT:
                        game.index_location += 1
                        if game.index_location >= len(game.sql.get_location(game.tournament.town)):
                            game.index_location = 0

            # manage the keybord used for update the score
            else:
                if game.next_up is False:
                    if game.game_statut:
                        if game.round.settings:
                            letters = {x: pygame.key.key_code(
                                x) for x in "1234567890"}
                            touche = pygame.key.get_pressed()
                            for (l, value) in letters.items():
                                if touche[value]:
                                    for player in game.round.players:
                                        if player.selected:
                                            player.score = int(
                                                str(player.score) + str(l))
                                            if player.score > 14:
                                                player.score = 14

                            if event.key == pygame.K_BACKSPACE:
                                for player in game.round.players:
                                    if player.selected:
                                        player.score = 0
