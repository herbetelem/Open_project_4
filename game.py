import pygame
from tournament import Tournament
from SQL_function import SQL_function
from add_player import Add_player

# create class game


class Game:

    def __init__(self, screen):

        # var for the program
        self.is_launch = False
        self.screen = screen
        self.step = False
        self.background = pygame.image.load('assets/bg-2.jpeg')
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.sql = SQL_function()
        self.next = pygame.image.load('assets/button/next.png')
        self.next = pygame.transform.scale(self.next, (400, 150))
        self.next_rect = self.next.get_rect()
        self.next_rect.x = (1280 - 400) / 2
        self.next_rect.y = 500
        self.font = pygame.font.Font(None, 55)
        self.font_turn = pygame.font.Font(None, 90)
        self.search_button = pygame.image.load('assets/button/search.png')
        self.search_button = pygame.transform.scale(
            self.search_button, (50, 50))
        self.search_button_rect = self.search_button.get_rect()
        self.search_button_rect.x = 940
        self.search_button_rect.y = 125

        # var about the tournament
        self.players = []
        self.tournament = Tournament()
        self.index_location = 0
        self.set_time()
        self.more = self.font_turn.render("+", 1, (255, 255, 255))
        self.more_rect = self.more.get_rect()
        self.more_rect.x = 400
        self.more_rect.y = 300
        self.less = self.font_turn.render("-", 1, (255, 255, 255))
        self.less_rect = self.less.get_rect()
        self.less_rect.x = 800
        self.less_rect.y = 300
        self.choice = 1
        self.set_round_time()
        self.players = []
        self.players_search = ""
        self.tmp_players = []
        list_search_location = [[245, 190], [345, 190], [445, 190], [
            545, 190], [245, 640], [345, 640], [445, 640], [545, 640]]
        for i in list_search_location:
            self.tmp_players.append(Add_player(i[0], i[1], False, 0))

    # set the rect for the time management

    def set_time(self):
        font_date = pygame.font.Font(None, 70)
        self.day = 1
        self.day_font = font_date.render(str(self.day), 1, (255, 255, 255))
        self.day_rect = self.day_font.get_rect()
        self.day_rect.x = 400
        self.day_rect.y = 300
        self.month = 1
        self.month_font = font_date.render(str(self.month), 1, (255, 255, 255))
        self.month_rect = self.month_font.get_rect()
        self.month_rect.x = 620
        self.month_rect.y = 300
        self.year = 2021
        self.year_font = font_date.render(str(self.year), 1, (255, 255, 255))
        self.year_rect = self.year_font.get_rect()
        self.year_rect.x = 840
        self.year_rect.y = 300

    # method for update the game
    def update(self, screen):
        # app the background
        screen.blit(self.background, (0, 0))
        # if we want to create a tournament
        self.create_tournament(screen)

    # methode to create the tournament
    def create_tournament(self, screen):
        if self.step == "name":
            self.create_tournament_name(screen)
        elif self.step == "country":
            self.create_tournament_country(screen)
        elif self.step == "town":
            self.create_tournament_town(screen)
        elif self.step == "location":
            self.create_tournament_location(screen)
        elif self.step == "date":
            self.create_tournament_date(screen)
        elif self.step == "turn":
            self.create_tournament_turn(screen)
        elif self.step == "tour":
            self.create_tournament_tour(screen)
        elif self.step == "time":
            self.create_tournament_time(screen)
        elif self.step == "description":
            self.create_tournament_description(screen)
        elif self.step == "player":
            self.create_tournament_player(screen)
        elif self.step == "end":
            self.create_tournament_end(screen)
        elif self.step == "next":
            self.resume_tournament(screen)

    # methode to create the name
    def create_tournament_name(self, screen):
        sentence = "Veuillez entrer le nom du tournoi"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 100))
        input = pygame.image.load('assets/button/input.png')
        input = pygame.transform.scale(input, (700, 150))
        screen.blit(input, (((1280 - 700) / 2), 300))
        text = self.font.render(self.tournament.name, 1, (255, 255, 255))
        screen.blit(text, (((1280 - 700) / 2 + 50), 340))
        screen.blit(self.next, self.next_rect)

    # method to select the country
    def create_tournament_country(self, screen):
        sentence = "Veuillez choisir le pays"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (440, 100))
        screen.blit(self.next, self.next_rect)
        country = self.sql.get_country()
        country_tmp = pygame.font.Font(None, 130).render(
            "<  " + country[self.index_location][1] + "  >",
            1,
            (255, 255, 255))
        screen.blit(country_tmp, (420, 300))

    def create_tournament_town(self, screen):
        sentence = "Veuillez choisir la ville"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (440, 100))
        screen.blit(self.next, self.next_rect)
        town = self.sql.get_town(self.tournament.country)
        town_tmp = pygame.font.Font(None, 130).render(
            "<  " + town[self.index_location][1] + "  >",
            1,
            (255, 255, 255))
        screen.blit(town_tmp, (420, 300))

    def create_tournament_location(self, screen):
        sentence = "Veuillez choisir le batiment"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (440, 100))
        screen.blit(self.next, self.next_rect)
        location = self.sql.get_location(self.tournament.town)
        location_tmp = pygame.font.Font(None, 130).render(
            "<  " + location[self.index_location][2] + "  >",
            1,
            (255, 255, 255))
        screen.blit(location_tmp, (220, 300))

    def create_tournament_date(self, screen):
        font_date = pygame.font.Font(None, 70)
        sentence = "Veuillez choisir la date"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (440, 100))
        screen.blit(self.next, self.next_rect)
        self.day_font = font_date.render(str(self.day), 1, (255, 255, 255))
        self.month_font = font_date.render(str(self.month), 1, (255, 255, 255))
        self.year_font = font_date.render(str(self.year), 1, (255, 255, 255))
        screen.blit(self.day_font, self.day_rect)
        screen.blit(self.month_font, self.month_rect)
        screen.blit(self.year_font, self.year_rect)

    def create_tournament_turn(self, screen):
        font_turn = pygame.font.Font(None, 70)
        sentence = "Veuillez choisir le nombre de tours"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 100))
        screen.blit(self.next, self.next_rect)
        turn = font_turn.render(
            str(self.tournament.nb_turn), 1, (255, 255, 255))
        screen.blit(turn, (600, 300))
        screen.blit(self.more, self.more_rect)
        screen.blit(self.less, self.less_rect)

    def create_tournament_time(self, screen):
        sentence = "Veuillez choisir le style de temps"
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 100))
        screen.blit(self.next, self.next_rect)
        self.set_round_time()
        screen.blit(self.choice_A, self.choice_A_rect)
        screen.blit(self.choice_B, self.choice_B_rect)
        screen.blit(self.choice_C, self.choice_C_rect)
        text_A = self.font.render("bullet", 1, (255, 255, 255))
        text_B = self.font.render("blitz", 1, (255, 255, 255))
        text_C = self.font.render("coup rapide", 1, (255, 255, 255))
        screen.blit(text_A, (130, 310))
        screen.blit(text_B, (530, 310))
        screen.blit(text_C, (930, 310))

    def set_round_time(self):
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

    def create_tournament_description(self, screen):
        sentence = "Veuillez entrer la description du tournoi"
        font = pygame.font.Font(None, 35)
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 100))
        input = pygame.image.load('assets/button/input.png')
        input = pygame.transform.scale(input, (700, 150))
        screen.blit(input, (((1280 - 700) / 2), 300))
        text_tmp = self.tournament.description
        text_y = 320
        while len(text_tmp) > 0:
            text = font.render(text_tmp[:50], 1, (255, 255, 255))
            screen.blit(text, (((1280 - 700) / 2 + 10), text_y))
            text_tmp = text_tmp[50:]
            text_y += 30
        screen.blit(self.next, self.next_rect)

    def create_tournament_player(self, screen):
        tmp_p = 8 - len(self.players)
        sentence = f"Veuillez selectioner les {tmp_p} joueurs"
        font = pygame.font.Font(None, 35)
        text = self.font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 50))
        if len(self.players) == 8:
            screen.blit(self.next, self.next_rect)
        else:
            input = pygame.image.load('assets/button/input.png')
            input = pygame.transform.scale(input, (600, 75))
            screen.blit(input, (310, 100))
            screen.blit(self.search_button, self.search_button_rect)
            text = font.render(self.players_search, 1, (255, 255, 255))
            screen.blit(text, (330, 120))
            text = font.render("nom du joueur", 1, (255, 255, 255))
            screen.blit(text, (120, 120))
            self.search_player(screen)

    def search_player(self, screen):
        if len(self.players_search) > 0:
            request = self.sql.get_players(self.players_search)
            index = 0
            tmp_x = 250
            tmp_y = 250
            for tmp in self.tmp_players:
                tmp.show = False
            for player in request:
                font = pygame.font.Font(None, 35)
                name = player[1] + " " + player[2]
                text = font.render(name, 1, (255, 255, 255))
                screen.blit(text, (tmp_x, tmp_y))
                if index == 3:
                    tmp_y = 250
                    tmp_x = 700
                else:
                    tmp_y += 100
                self.tmp_players[index].show = True
                self.tmp_players[index].id_player = player[0]
                index += 1
            for tmp in self.tmp_players:
                if tmp.show == True:
                    if tmp.id_player not in self.players:
                        screen.blit(tmp.img, tmp.rect)

    def create_tournament_end(self, screen):
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

    def resume_tournament(self, screen):
        sentence = f"Résumé du tournoi"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 50))
        sentence = f"nom: {self.tournament.name}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 100))
        sentence = f"pays: {self.tournament.country}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 150))
        sentence = f"ville: {self.tournament.town}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 200))
        sentence = f"lieu: {self.tournament.location}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 250))
        sentence = f"date: {self.tournament.date}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 300))
        sentence = f"temps: {self.tournament.time}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 350))
        sentence = f"description: {self.tournament.description}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 400))
        sentence = f"joueurs: {self.tournament.players}"
        font = pygame.font.Font(None, 35)
        text = font.render(sentence, 1, (255, 255, 255))
        screen.blit(text, (340, 450))
        