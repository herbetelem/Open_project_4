import pygame
from turtle import pd

from add_player import Add_player
from date_select import Date_selected
from load_a_tournament import Load_a_tournament
from round import Round
from SQL_function import SQL_function
from tournament import Tournament

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
        self.load = False
        self.match_load = False
        self.history_button = []
        self.sql = SQL_function()

        # set the different background
        self.background = self.set_an_image('assets/bg-2.jpeg', (1280, 720))
        self.background_2 = self.set_an_image('assets/bg-3.jpeg', (1280, 720))
        self.background_3 = self.set_an_image('assets/bg-4.jpeg', (1280, 720))

        # set the button next or start
        self.next = self.set_an_image('assets/button/next.png', (400, 150))
        self.next_rect = self.set_an_image_rec(
            self.next, (1280 - 400) / 2, 500)
        self.start = self.set_an_image('assets/button/start.png', (400, 150))
        self.start_rect = self.set_an_image_rec(
            self.start, (1280 - 400) / 2, 500)
        self.search_button = self.set_an_image(
            'assets/button/search.png', (50, 50))
        self.search_button_rect = self.set_an_image_rec(
            self.search_button, 940, 125)
        self.prev = self.set_an_image('assets/button/prev.png', (400, 150))
        self.prev_rect = self.set_an_image_rec(
            self.prev, (1280 - 400) / 2, 500)

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
        self.choice_A = ""
        self.choice_B = ""
        self.choice_C = ""
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
            "country": self.create_tournament_place,
            "town": self.create_tournament_place,
            "location": self.create_tournament_place,
            "date": self.create_tournament_date,
            "time": self.create_tournament_time,
            "description": self.create_tournament_description,
            "player": self.create_tournament_player,
            "end": self.create_tournament_end,
            "next": self.resume_tournament
        }

    def set_var_game(self):
        """ Method who will set the variables that will be used for game """

        #  set the button object tha will be used for the management of the tournament
        self.game_statut = True
        self.validate = self.set_an_image(
            'assets/button/validate.png', (150, 50))
        self.validate_rect = self.set_an_image_rec(self.validate, 550, 650)
        self.update_score = self.set_an_image(
            'assets/button/setting.png', (50, 50))
        self.update_score_rect = self.set_an_image_rec(
            self.update_score, 750, 650)
        self.save = self.set_an_image('assets/button/save.png', (150, 50))
        self.save_rect = self.set_an_image_rec(self.save, 600, 600)
        self.round = Round(self.players, self.tournament.id)
        self.round.generate_round()
        self.player_selected = 0

        # generate all the desck object
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

        deck = self.set_an_image('assets/match-no-result.png', (140, 140))
        deck_rect = self.set_an_image_rec(deck, deck_rect_x, deck_rect_y)
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

        # load the histry of tournament
        if self.load:
            self.screen.blit(self.background_3, (0, 0))
            self.show_prev_matchs()
        # load the tournament
        elif self.tournament.created:
            # app the background
            self.screen.blit(self.background_2, (0, 0))
            if self.round.settings:
                self.show_settings()
            elif self.game_statut:
                self.show_match()
            else:
                self.show_result()
        # load the creation of the tournament
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

        self.print_sentence("Please enter the name of the tournament")
        input = self.set_an_image('assets/button/input.png', (700, 150))
        self.screen.blit(input, (((1280 - 700) / 2), 300))
        text = self.font.render(self.tournament.name, 1, (255, 255, 255))
        self.screen.blit(text, (((1280 - 700) / 2 + 50), 340))
        if len(self.tournament.name) > 0:
            self.screen.blit(self.next, self.next_rect)

    def create_tournament_place(self):
        """ Method for select the tournament's country """

        if self.step == "country":
            sentence = "Please, choose the country"
            self.print_sentence(sentence)
            self.screen.blit(self.next, self.next_rect)
            data = self.sql.get_country()
        elif self.step == "town":
            sentence = "Please, choose the town"
            self.print_sentence(sentence)
            self.screen.blit(self.next, self.next_rect)
            data = self.sql.get_town(self.tournament.country)
        elif self.step == "location":
            sentence = "Please, choose the location"
            self.print_sentence(sentence)
            self.screen.blit(self.next, self.next_rect)
            data = self.sql.get_location(self.tournament.town)

        sentence_tmp = pygame.font.Font(None, 130).render(
            "<  " + str(data[self.index_location][1]) + "  >",
            1,
            (255, 255, 255))
        self.screen.blit(sentence_tmp, (350, 300))

    def create_tournament_date(self):
        """ Method for select the tournament's date """

        font_date = pygame.font.Font(None, 70)
        self.print_sentence("Please choose the date")
        self.screen.blit(self.next, self.next_rect)
        self.print_sentence(str(self.day.str), font_date, self.day.rect)
        self.print_sentence(str(self.month.str), font_date, self.month.rect)
        self.print_sentence(str(self.year.str), font_date, self.year.rect)

    def create_tournament_time(self):
        """ Methode for select the type of time """

        self.print_sentence("Please choose the time style")
        self.screen.blit(self.next, self.next_rect)
        self.set_round_time()
        self.screen.blit(self.choice_A, self.choice_A_rect)
        self.screen.blit(self.choice_B, self.choice_B_rect)
        self.screen.blit(self.choice_C, self.choice_C_rect)
        self.print_sentence("bullet", self.font, (130, 310))
        self.print_sentence("blitz", self.font, (530, 310))
        self.print_sentence("speed shot", self.font, (930, 310))

    def set_time(self):
        """ Method for se't up the rect of time management """

        # set up the day month and year in pygame format

        self.day = Date_selected("%d", 400, 300)
        self.month = Date_selected("%m", 620, 300)
        self.year = Date_selected("%Y", 840, 300)

    def set_round_time(self):
        """ Methode for update the display of the time selector """

        self.choice_A = self.set_an_image('assets/button/round.png', (60, 60))
        self.choice_A_rect = self.set_an_image_rec(self.choice_A, 50, 300)
        self.choice_B = self.set_an_image('assets/button/round.png', (60, 60))
        self.choice_B_rect = self.set_an_image_rec(self.choice_B, 450, 300)
        self.choice_C = self.set_an_image('assets/button/round.png', (60, 60))
        self.choice_C_rect = self.set_an_image_rec(self.choice_C, 850, 300)

        if self.choice == 1:
            self.choice_A = self.set_an_image(
                'assets/button/round_selected.png', (60, 60))
        if self.choice == 2:
            self.choice_B = self.set_an_image(
                'assets/button/round_selected.png', (60, 60))
        if self.choice == 3:
            self.choice_C = self.set_an_image(
                'assets/button/round_selected.png', (60, 60))

    def create_tournament_description(self):
        """ Methode for write the description of the tournament """

        self.print_sentence("Please enter the tournament's description")
        input = self.set_an_image('assets/button/input.png', (700, 150))
        self.screen.blit(input, (((1280 - 700) / 2), 300))
        text_tmp = self.tournament.description
        text_y = 320
        while len(text_tmp) > 0:
            font = pygame.font.Font(None, 35)
            self.print_sentence(
                text_tmp[:50], font, (((1280 - 700) / 2 + 10), text_y))
            text_tmp = text_tmp[50:]
            text_y += 30
        if len(self.tournament.description) > 0:
            self.screen.blit(self.next, self.next_rect)

    def create_tournament_player(self):
        """ Methode for select the player of the tournament """

        tmp_p = 8 - len(self.players)
        self.print_sentence(
            f"Please select the {tmp_p} players", self.font, (340, 50))

        # check if all the players have been selected
        if len(self.players) == 8:
            self.screen.blit(self.next, self.next_rect)
        else:
            input = self.set_an_image('assets/button/input.png', (600, 75))
            self.screen.blit(input, (310, 100))
            self.screen.blit(self.search_button, self.search_button_rect)
            self.print_sentence(self.players_search, self.font, (330, 120))
            self.print_sentence("player name", self.font, (20, 120))
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
        self.tournament.id = self.sql.get_tournament_id(
            [self.tournament.name, self.tournament.description, self.tournament.date])
        self.tournament.id = self.tournament.id[0][0]
        self.step = "next"

    def resume_tournament(self):
        """Method to resume the informations of the tournament """

        list_resume = [["Tournament resume", pygame.font.Font(None, 35), (340, 50)],
                       [f"Name: {self.tournament.name}",
                           pygame.font.Font(None, 35), (340, 100)],
                       [f"Country: {self.tournament.country}",
                           pygame.font.Font(None, 35), (340, 150)],
                       [f"Town: {self.tournament.town}",
                           pygame.font.Font(None, 35), (340, 200)],
                       [f"Location: {self.tournament.location}",
                           pygame.font.Font(None, 35), (340, 250)],
                       [f"Date: {self.tournament.date}",
                           pygame.font.Font(None, 35), (340, 300)],
                       [f"Time: {self.tournament.time}",
                           pygame.font.Font(None, 35), (340, 350)],
                       [f"Description: {self.tournament.description}",
                           pygame.font.Font(None, 35), (340, 400)],
                       [f"Players: {self.tournament.players}", pygame.font.Font(None, 35), (340, 450)]]
        for resume in list_resume:
            self.print_sentence(resume[0], resume[1], resume[2])
        self.screen.blit(self.start, self.start_rect)
        self.next_up = False

    # Method about the tournament
    def show_match(self):
        """ Method who will show the match of the actual round """

        self.print_sentence(
            f"Round match list n°{self.round.nb_turn + 1}", self.font, (400, 50))

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
        for index in range(1, 9):
            self.print_sentence(
                f"Place {index}: {self.round.players[index-1].name} {self.round.players[index-1].last_name}, score = {self.round.players[index-1].score}", self.font, (x, y))
            y += 70
        self.screen.blit(self.save, self.save_rect)

    def show_settings(self):
        """ Method for show the score during a tournament and edit it """

        self.round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 9):
            self.print_sentence(
                f"Place {index}: {self.round.players[index-1].name} {self.round.players[index-1].last_name}, score = {self.round.players[index-1].score}", self.font, (x, y))
            y += 70
        self.screen.blit(self.validate, self.validate_rect)
        x = 900
        y = 40
        for player in self.round.players:
            player.rect = self.set_an_image_rec(player.img, x, y)
            self.screen.blit(player.img, player.rect)
            y += 70

    # Method about the load of prev game
    def show_prev_matchs(self):
        if self.match_load:
            load = self.sql.get_players_score(self.match_load)
            x = 50
            y = 50
            for data in load:
                self.print_sentence(
                    f"{data[0]} {data[1]} score: {data[2]}", self.font, (x, y))
                y += 50
            self.screen.blit(self.prev, self.prev_rect)

        else:
            self.history = self.sql.get_prev_tournament()
            x = 50
            y = 50
            self.history_button = []
            for tournament in self.history:
                self.history_button.append(
                    Load_a_tournament(y, x+1000, tournament[0][0]))
                self.print_sentence(tournament[0][1], self.font, (x, y))
                y += 50
                self.print_sentence(tournament[0][2], self.font, (x, y))
                y += 50
            for index in self.history_button:
                self.screen.blit(index.img, index.rect)

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

    def set_an_image_rec(self, img, x, y):
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
