import pygame
from tournament import Tournament
from SQL_function import SQL_function
from add_player import Add_player
from datetime import datetime
from round import Round

# create class game


class Game:

    def __init__(self, screen):
        """ Object who will handle the game and the different step of it

        Args:
            screen (object pygame): the object of the screen
        """

        self.set_var_program(screen)
        self.set_var_tournament()

    # Method to init the var -------------------------
    def set_var_program(self, screen):
        """ Method who will set the variables that will be used for the program.

        Args:
            screen (object pygame): the object of the screen
        """

        # set the variable or object
        self.is_launch = False
        self.screen = screen
        self.step = False
        self.sql = SQL_function()

        # set the different background
        self.background = self.set_an_image('assets/bg-2.jpeg', (1280, 720))
        self.background_2 = self.set_an_image('assets/bg-3.jpeg', (1280, 720))

        # set the button next or start
        self.next = self.set_an_image('assets/button/next.png', '400, 150')
        self.next = pygame.image.load('assets/button/next.png')
        self.next = pygame.transform.scale(self.next, (400, 150))
        self.next_rect = self.next.get_rect()
        self.next_rect.x = (1280 - 400) / 2
        self.next_rect.y = 500
        self.start = pygame.image.load('assets/button/start.png')
        self.start = pygame.transform.scale(self.start, (400, 150))
        self.start_rect = self.start.get_rect()
        self.start_rect.x = (1280 - 400) / 2
        self.start_rect.y = 500
        self.search_button = pygame.image.load('assets/button/search.png')
        self.search_button = pygame.transform.scale(
            self.search_button, (50, 50))
        self.search_button_rect = self.search_button.get_rect()
        self.search_button_rect.x = 940
        self.search_button_rect.y = 125
        self.next_up = True

        # set the font
        self.font = pygame.font.Font(None, 55)
        self.font_turn = pygame.font.Font(None, 90)

    def set_var_tournament(self):
        """ Method who will set the variables that will be used for the tournament """
        # var about the tournament
        self.players = []
        self.tournament = Tournament()
        self.index_location = 0
        self.set_time()
        self.choice = 1
        self.set_round_time()

        # set the button more and less
        self.more = self.font_turn.render("+", 1, (255, 255, 255))
        self.more_rect = self.more.get_rect()
        self.more_rect.x = 400
        self.more_rect.y = 300
        self.less = self.font_turn.render("-", 1, (255, 255, 255))
        self.less_rect = self.less.get_rect()
        self.less_rect.x = 800
        self.less_rect.y = 300

        # set the players
        self.players = []
        self.players_search = ""
        self.tmp_players = []
        list_search_location = [[245, 190], [345, 190], [445, 190], [
            545, 190], [245, 640], [345, 640], [445, 640], [545, 640]]
        for i in list_search_location:
            self.tmp_players.append(Add_player(i[0], i[1], False, 0))

        # all method for the create
        self.switch_tournament = {
            "name": self.create_tournament_name,
            "country": self.create_tournament_country,
            "town": self.create_tournament_town,
            "location": self.create_tournament_location,
            "date": self.create_tournament_date,
            "time": self.create_tournament_time,
            "description": self.create_tournament_description,
            "player": self.create_tournament_player,
            "end": self.create_tournament_end,
            "next": self.resume_tournament
        }

    def set_var_game(self):
        """ Method who will set the variables that will be used for game """

        self.game_statut = True

        self.validate = pygame.image.load('assets/button/validate.png')
        self.validate = pygame.transform.scale(self.validate, (150, 50))
        self.validate_rect = self.validate.get_rect()
        self.validate_rect.x = 550
        self.validate_rect.y = 650
        self.update_score = pygame.image.load('assets/button/setting.png')
        self.update_score = pygame.transform.scale(self.update_score, (50, 50))
        self.update_score_rect = self.update_score.get_rect()
        self.update_score_rect.x = 750
        self.update_score_rect.y = 650

        self.round = Round(self.players)
        self.round.generate_round()

        deck_tmp = self.generate_var_game(275, 150, 50, 200, 450, 200)
        self.deck_1 = deck_tmp[0]
        self.deck_1_rect = deck_tmp[1]
        self.player_1_rect = deck_tmp[2]
        self.player_2_rect = deck_tmp[3]
        self.area_win_1 = deck_tmp[4]
        self.area_rect_win_1 = deck_tmp[5]
        self.area_win_2 = deck_tmp[6]
        self.area_rect_win_2 = deck_tmp[7]

        deck_tmp = self.generate_var_game(275, 450, 50, 490, 450, 490)
        self.deck_2 = deck_tmp[0]
        self.deck_2_rect = deck_tmp[1]
        self.player_3_rect = deck_tmp[2]
        self.player_4_rect = deck_tmp[3]
        self.area_win_3 = deck_tmp[4]
        self.area_rect_win_3 = deck_tmp[5]
        self.area_win_4 = deck_tmp[6]
        self.area_rect_win_4 = deck_tmp[7]

        deck_tmp = self.generate_var_game(875, 150, 650, 200, 1050, 200)
        self.deck_3 = deck_tmp[0]
        self.deck_3_rect = deck_tmp[1]
        self.player_5_rect = deck_tmp[2]
        self.player_6_rect = deck_tmp[3]
        self.area_win_5 = deck_tmp[4]
        self.area_rect_win_5 = deck_tmp[5]
        self.area_win_6 = deck_tmp[6]
        self.area_rect_win_6 = deck_tmp[7]

        deck_tmp = self.generate_var_game(875, 450, 650, 490, 1050, 490)
        self.deck_4 = deck_tmp[0]
        self.deck_4_rect = deck_tmp[1]
        self.player_7_rect = deck_tmp[2]
        self.player_8_rect = deck_tmp[3]
        self.area_win_7 = deck_tmp[4]
        self.area_rect_win_7 = deck_tmp[5]
        self.area_win_8 = deck_tmp[6]
        self.area_rect_win_8 = deck_tmp[7]

    def generate_var_game(self, deck_rect_x, deck_rect_y, area_A_x, area_A_y, area_B_x, area_B_y):
        """Method to generate the desck and player pygame object

        Args:
            deck_rect_x (int): rect X of the desk
            deck_rect_y (int): rect Y of the desk
            area_A_x (int): rect X of the Player A
            area_A_y (int): rect Y of the Player A
            area_B_x (int): rect X of the Player B
            area_B_y (int): rect Y of the Player B

        Returns:
            tuple: all pygame object
        """

        deck = pygame.image.load('assets/match-no-result.png')
        deck = pygame.transform.scale(deck, (140, 140))
        deck_rect = deck.get_rect()
        deck_rect.x = deck_rect_x
        deck_rect.y = deck_rect_y
        area_win_A = pygame.Rect((area_A_x, area_A_y), (150, 40))
        area_rect_win_A = pygame.Surface(area_win_A.size)
        area_rect_win_A.set_alpha(0)
        area_win_B = pygame.Rect((area_B_x, area_B_y), (150, 40))
        area_rect_win_B = pygame.Surface(area_win_B.size)
        area_rect_win_B.set_alpha(0)

        return deck, deck_rect, '', '', area_win_A, area_rect_win_A, area_win_B, area_rect_win_B

    #  Method to manage all
    def update(self):
        """ Method who will call the function for the actual step of the programm """

        if self.tournament.created:
            # app the background
            self.screen.blit(self.background_2, (0, 0))
            if self.round.settings:
                self.show_settings()
            elif self.game_statut:
                self.show_match()
            else:
                self.show_result()
        else:
            # app the background
            self.screen.blit(self.background, (0, 0))
            # if we want to create a tournament
            self.create_tournament()

    # Method about the creation
    def create_tournament(self):
        """ Method to manage the step of creation of the Tournament """

        self.switch_tournament.get(self.step, self.create_tournament_name)()

    def create_tournament_name(self):
        """ Method for create the tournament's name """

        self.print_sentence("Veuillez entrer le nom du tournoi")
        input = pygame.image.load('assets/button/input.png')
        input = pygame.transform.scale(input, (700, 150))
        self.screen.blit(input, (((1280 - 700) / 2), 300))
        text = self.font.render(self.tournament.name, 1, (255, 255, 255))
        self.screen.blit(text, (((1280 - 700) / 2 + 50), 340))
        self.screen.blit(self.next, self.next_rect)

    def create_tournament_country(self):
        """ Method for select the tournament's country """

        # suprimer les 2 methode d'en dessous, et faire celle si generique avec un elif degueu pour country ville et location

        sentence = "Veuillez choisir le pays"
        self.print_sentence(sentence)
        self.screen.blit(self.next, self.next_rect)

        country = self.sql.get_country()
        country_tmp = pygame.font.Font(None, 130).render(
            "<  " + country[self.index_location][1] + "  >",
            1,
            (255, 255, 255))
        self.screen.blit(country_tmp, (420, 300))

    def create_tournament_town(self):
        """ Method for select the tournament's town """

        self.print_sentence("Veuillez choisir la ville")
        self.screen.blit(self.next, self.next_rect)
        town = self.sql.get_town(self.tournament.country)
        town_tmp = pygame.font.Font(None, 130).render(
            "<  " + town[self.index_location][1] + "  >",
            1,
            (255, 255, 255))
        self.screen.blit(town_tmp, (420, 300))

    def create_tournament_location(self):
        """ Method for select the tournament's location """

        self.print_sentence("Veuillez choisir le batiment")
        self.screen.blit(self.next, self.next_rect)
        location = self.sql.get_location(self.tournament.town)
        location_tmp = pygame.font.Font(None, 130).render(
            "<  " + location[self.index_location][2] + "  >",
            1,
            (255, 255, 255))
        self.screen.blit(location_tmp, (220, 300))

    def create_tournament_date(self):
        """ Method for select the tournament's date """

        font_date = pygame.font.Font(None, 70)
        self.print_sentence("Veuillez choisir la date")
        self.screen.blit(self.next, self.next_rect)
        self.print_sentence(str(self.day), font_date, self.day_rect)
        self.print_sentence(str(self.month), font_date, self.month_rect)
        self.print_sentence(str(self.year), font_date, self.year_rect)

    def create_tournament_time(self):
        """ Methode for select the type of time """

        self.print_sentence("Veuillez choisir le style de temps")
        self.screen.blit(self.next, self.next_rect)
        self.set_round_time()
        self.screen.blit(self.choice_A, self.choice_A_rect)
        self.screen.blit(self.choice_B, self.choice_B_rect)
        self.screen.blit(self.choice_C, self.choice_C_rect)
        self.print_sentence("bullet", self.font, (130, 310))
        self.print_sentence("blitz", self.font, (530, 310))
        self.print_sentence("coup rapide", self.font, (930, 310))

    def set_time(self):
        """ Method for se't up the rect of time management """

        # set up the day month and year in pygame format

        #  RENDRE GENERIQUE
        font_date = pygame.font.Font(None, 70)
        self.day = int(datetime.now().strftime('%d'))
        self.day_font = font_date.render(str(self.day), 1, (255, 255, 255))
        self.day_rect = self.day_font.get_rect()
        self.day_rect.x = 400
        self.day_rect.y = 300
        self.month = int(datetime.now().strftime('%m'))
        self.month_font = font_date.render(str(self.month), 1, (255, 255, 255))
        self.month_rect = self.month_font.get_rect()
        self.month_rect.x = 620
        self.month_rect.y = 300
        self.year = int(datetime.now().strftime('%Y'))
        self.year_font = font_date.render(str(self.year), 1, (255, 255, 255))
        self.year_rect = self.year_font.get_rect()
        self.year_rect.x = 840
        self.year_rect.y = 300

    def set_round_time(self):
        """ Methode for update the display of the time selector """


        #  rendre generique avec un dico
        if(self.choice == 1):
            self.choice_A = pygame.image.load(
                'assets/button/round_selected.png')
        else:
            self.choice_A = pygame.image.load('assets/button/round.png')
        self.choice_A = pygame.transform.scale(self.choice_A, (60, 60))
        self.choice_A_rect = self.choice_A.get_rect()
        self.choice_A_rect.x = 50
        self.choice_A_rect.y = 300

        if(self.choice == 2):
            self.choice_B = pygame.image.load(
                'assets/button/round_selected.png')
        else:
            self.choice_B = pygame.image.load('assets/button/round.png')
        self.choice_B = pygame.transform.scale(self.choice_B, (60, 60))
        self.choice_B_rect = self.choice_B.get_rect()
        self.choice_B_rect.x = 450
        self.choice_B_rect.y = 300

        if(self.choice == 3):
            self.choice_C = pygame.image.load(
                'assets/button/round_selected.png')
        else:
            self.choice_C = pygame.image.load('assets/button/round.png')
        self.choice_C = pygame.transform.scale(self.choice_C, (60, 60))
        self.choice_C_rect = self.choice_C.get_rect()
        self.choice_C_rect.x = 850
        self.choice_C_rect.y = 300

    def create_tournament_description(self):
        """ Methode for write the description of the tournament """

        self.print_sentence("Veuillez entrer la description du tournoi")
        input = pygame.image.load('assets/button/input.png')
        input = pygame.transform.scale(input, (700, 150))
        self.screen.blit(input, (((1280 - 700) / 2), 300))
        text_tmp = self.tournament.description
        text_y = 320
        while len(text_tmp) > 0:
            font = pygame.font.Font(None, 35)
            self.print_sentence(
                text_tmp[:50], font, (((1280 - 700) / 2 + 10), text_y))
            text_tmp = text_tmp[50:]
            text_y += 30
        self.screen.blit(self.next, self.next_rect)

    def create_tournament_player(self):
        """ Methode for select the player of the tournament """

        tmp_p = 8 - len(self.players)
        self.print_sentence(
            f"Veuillez selectioner les {tmp_p} joueurs", self.font, (340, 50))

        # check if all the players have been selected
        if len(self.players) == 8:
            self.screen.blit(self.next, self.next_rect)
        else:
            input = pygame.image.load('assets/button/input.png')
            input = pygame.transform.scale(input, (600, 75))
            self.screen.blit(input, (310, 100))
            self.screen.blit(self.search_button, self.search_button_rect)
            self.print_sentence(self.players_search, self.font, (330, 120))
            self.print_sentence("nom du joueur", self.font, (20, 120))
            self.search_player()

    def search_player(self):
        """ method to search the players """

        if len(self.players_search) > 0:
            # get the list of player in the bdd
            request = self.sql.get_players(self.players_search)
            index = 0
            tmp_x = 250
            tmp_y = 250

            # set up the button to false, in case of less than 8 result
            for tmp in self.tmp_players:
                tmp.show = False
            for player in request:
                font = pygame.font.Font(None, 35)
                self.print_sentence(
                    player[1] + " " + player[2], font, (tmp_x, tmp_y))
                if index == 3:
                    tmp_y = 250
                    tmp_x = 700
                else:
                    tmp_y += 100
                self.tmp_players[index].show = True
                self.tmp_players[index].id_player = player[0]
                index += 1

            # check if the player has been already selected or if the button have to be seen
            for tmp in self.tmp_players:
                if tmp.show:
                    if tmp.id_player not in self.players:
                        self.screen.blit(tmp.img, tmp.rect)

    def create_tournament_end(self):
        """ Method to save the tournament in the bdd """
        # save the tournament in the db
        data = (self.tournament.name,
                self.tournament.location[0],
                self.tournament.nb_turn,
                self.tournament.description,
                self.tournament.time,
                self.tournament.date
                )
        self.sql.create_tournament(data, self.players)
        self.step = "next"

    def resume_tournament(self):
        """Method to resume the informations of the tournament """

        # test generique ([label, valeur, position])
        self.print_sentence("Résumé du tournoi",
                            pygame.font.Font(None, 35), (340, 50))
        self.print_sentence(
            f"nom: {self.tournament.name}", pygame.font.Font(None, 35), (340, 100))
        self.print_sentence(
            f"pays: {self.tournament.country}", pygame.font.Font(None, 35), (340, 150))
        self.print_sentence(
            f"ville: {self.tournament.town}", pygame.font.Font(None, 35), (340, 200))
        self.print_sentence(f"lieu: {self.tournament.location}",
                            pygame.font.Font(None, 35), (340, 250))
        self.print_sentence(
            f"date: {self.tournament.date}", pygame.font.Font(None, 35), (340, 300))
        self.print_sentence(
            f"temps: {self.tournament.time}", pygame.font.Font(None, 35), (340, 350))
        self.print_sentence(
            f"description: {self.tournament.description}", pygame.font.Font(None, 35), (340, 400))
        self.print_sentence(
            f"joueurs: {self.tournament.players}", pygame.font.Font(None, 35), (340, 450))
        self.screen.blit(self.start, self.start_rect)
        self.next_up = False

    # Method about the tournament
    def show_match(self):
        """ Method who will show the match of the actual round """

        self.print_sentence(
            f"Liste des matchs du Round {self.round.nb_turn + 1}", self.font, (400, 50))

        # match 1
        self.print_sentence(
            f"{self.round.match[0][0].last_name[0]}.{self.round.match[0][0].name[:5]}", self.font, (50, 190))
        self.print_sentence(
            f"{self.round.match[0][1].last_name[0]}.{self.round.match[0][1].name[:5]}", self.font, (450, 190))
        self.screen.blit(self.deck_1, self.deck_1_rect)
        self.screen.blit(self.area_rect_win_1, self.area_win_1)
        self.screen.blit(self.area_rect_win_2, self.area_win_2)

        # match 2
        self.print_sentence(
            f"{self.round.match[1][0].last_name[0]}.{self.round.match[1][0].name[:5]}", self.font, (50, 490))
        self.print_sentence(
            f"{self.round.match[1][1].last_name[0]}.{self.round.match[1][1].name[:5]}", self.font, (450, 490))
        self.screen.blit(self.deck_2, self.deck_2_rect)
        self.screen.blit(self.area_rect_win_3, self.area_win_3)
        self.screen.blit(self.area_rect_win_4, self.area_win_4)

        # match 3
        self.print_sentence(
            f"{self.round.match[2][0].last_name[0]}.{self.round.match[2][0].name[:5]}", self.font, (650, 190))
        self.print_sentence(
            f"{self.round.match[2][1].last_name[0]}.{self.round.match[2][1].name[:5]}", self.font, (1050, 190))
        self.screen.blit(self.deck_3, self.deck_3_rect)
        self.screen.blit(self.area_rect_win_5, self.area_win_5)
        self.screen.blit(self.area_rect_win_6, self.area_win_6)

        # match 4
        self.print_sentence(
            f"{self.round.match[3][0].last_name[0]}.{self.round.match[3][0].name[:5]}", self.font, (650, 490))
        self.print_sentence(
            f"{self.round.match[3][1].last_name[0]}.{self.round.match[3][1].name[:5]}", self.font, (1050, 490))
        self.screen.blit(self.deck_4, self.deck_4_rect)
        self.screen.blit(self.area_rect_win_7, self.area_win_7)
        self.screen.blit(self.area_rect_win_8, self.area_win_8)

        # button validate and settings
        self.screen.blit(self.update_score, self.update_score_rect)
        tmp_check = True
        for match in self.round.match:
            if match[2] < 1:
                tmp_check = False

        if tmp_check:
            self.screen.blit(self.validate, self.validate_rect)

    def show_result(self):
        """ Method to show the result of the tournament
        """

        self.round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 8):
            self.print_sentence(
                f"Place {index}: {self.round.players[index-1].name} {self.round.players[index-1].last_name}, score = {self.round.players[index-1].score}", self.font, (x, y))
            y += 60


    def show_settings(self):
        """ Method for show the score during a tournament and edit it """

        self.round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 8):
            self.print_sentence(
                f"Place {index}: {self.round.players[index-1].name} {self.round.players[index-1].last_name}, score = {self.round.players[index-1].score}", self.font, (x, y))
            y += 60
        self.screen.blit(self.validate, self.validate_rect)

    # Method general
    def print_sentence(self, sentence, font=False, position=(340, 100)):
        """ the Methode to print a sentence in the game

        Args:
            sentence (string): the string to print
            font ([object pygame]): the font who will be use on the print
            position (tuple, optional): the position of the print. Defaults to (340, 100).
        """

        if not font:
            font = self.font
        text = font.render(sentence, 1, (255, 255, 255))
        self.screen.blit(text, position)

    def set_an_image(self, path, size=False):
        """ Method to set up an image

        Args:
            path (str): path to the image
            size (bool, optional): size of the images

        Returns:
            object: object img pygame
        """
        img = pygame.image.load(path)
        if size:
            img = pygame.transform.scale(img, size)
        return img

    def set_an_image(self, img, x, y):
        """ Method to set up an image

        Args:
            path (str): path to the image
            size (bool, optional): size of the images

        Returns:
            object: object img pygame resized
        """
        img_rect = img.get_rect()
        img_rect.x = x
        img_rect.y = y
        return img_rect
