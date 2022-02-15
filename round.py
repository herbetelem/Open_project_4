from calendar import c
from cgitb import reset
from datetime import datetime
from multiprocessing import pool
from pickle import FALSE
from re import A
from SQL_function import SQL_function
from player import Player


# create class round


class Round:

    def __init__(self, players):
        """ Class to manage the round

        Args:
            players (list): list of all players by id
        """

        self.sql = SQL_function()
        self.players = []
        self.group_A = []
        self.group_B = []
        self.date_start = datetime.now().strftime('%Y-%m-%d')
        self.date_end = ""
        self.hour_start =  datetime.now().strftime('%H-%M')
        self.hour_end = ""
        self.id_tournament = ""
        self.match = [[1, 2, False], [3, 4, False], [5, 6, False], [7, 8, False]]
        self.match_done = []
        self.nb_turn = 0
        players = self.sort_players(players)
        for player in players:
            self.players.append(Player(player[0], player[2], player[1], player[3]))

    def sort_players(self, players):
        """ method to sort the player by their global_rankd

        Args:
            players (list): list of players

        Returns:
            [type]: list of players with their rank
        """

        if self.nb_turn == 0:
            players = self.sql.get_players_rank(players)
            return players
        else:
            return

    def generate_round(self):
        """ Methode to generate the round """

        index_match = 0
        # set up all false cause for the new round no one have an adv for now
        list_adv = [False, False, False, False, False, False, False, False]
        list_order = [4, 5, 6, 7, 3, 2, 1, 0]
        for player in self.players:
            is_player_choosed = False
            for match in self.match:
                if player in match:
                    is_player_choosed = True
            
            if not is_player_choosed and index_match < 4:
                # for order in list_order:
                #     if self.players[order] not in player.matched and not list_adv[order]:
                #         self.match[index_match][0] = player
                #         self.match[index_match][1] = self.players[order]
                #         list_adv[order] = True
                #         is_player_choosed = True
                if self.players[4] not in player.matched and not list_adv[4]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[4]
                    list_adv[4] = True
                    is_player_choosed = True
                elif self.players[5] not in player.matched and not list_adv[5]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[5]
                    list_adv[5] = True
                    is_player_choosed = True
                elif self.players[6] not in player.matched and not list_adv[6]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[6]
                    list_adv[6] = True
                    is_player_choosed = True
                elif self.players[7] not in player.matched and not list_adv[7]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[7]
                    list_adv[7] = True
                    is_player_choosed = True
                elif self.players[3] not in player.matched and not list_adv[3]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[3]
                    list_adv[3] = True
                    is_player_choosed = True
                elif self.players[2] not in player.matched and not list_adv[2]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[2]
                    list_adv[2] = True
                    is_player_choosed = True
                elif self.players[1] not in player.matched and not list_adv[1]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[1]
                    list_adv[1] = True
                    is_player_choosed = True
                elif self.players[0] not in player.matched and not list_adv[0]:
                    self.match[index_match][0] = player
                    self.match[index_match][1] = self.players[0]
                    list_adv[0] = True
                    is_player_choosed = True
                index_match += 1

    def validate_round(self, results):
        """ Method to save the match

        Args:
            results (list): list of result of the match
        """

        for index in range(4):
            print(f"{self.match[index][0].id} {self.match[index][1].id}")
            if results[index] == 0:
                self.match[index][0].score += 1
                self.match[index][1].score += 1
            elif results[index] == 1:
                self.match[index][0].score += 2
                self.match[index][1].score += 0
            elif results[index] == 2:
                self.match[index][0].score += 0
                self.match[index][1].score += 2
            
            self.match[index][0].matched.append(self.match[index][1])
            self.match[index][1].matched.append(self.match[index][0])
        self.match = [[1, 2, False], [3, 4, False], [5, 6, False], [7, 8, False]]
        self.nb_turn += 1
        for player in self.players:
            player.choosed = False

    def print_score(self):
        """ Method to print the actual score (method for development only) """
        self.sort_by_rank()
        for player in self.players:
            print(f"{player.name} a {player.score}")

    def sort_by_rank(self):
        """ Method to sort the players first by their score, then by their global rank """

        for player in self.players:
            player.global_rank = player.global_rank * -1
        self.players.sort(key=lambda x: (x.score, x.global_rank) , reverse=True)
        for player in self.players:
            player.global_rank = player.global_rank * -1
        self.group_A = []
        self.group_B = []
        for i in range(8):
            if i < 4:
                self.players[i].pool = 1
                self.group_A.append(self.players[i])
            else:
                self.players[i].pool = 2
                self.group_B.append(self.players[i])
            self.players[i].pool_rank = i


# item = Round([301, 302, 303, 304, 205, 306, 208, 308])
# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.generate_round()
# item.validate_round([1,0,2,1])

# item.print_score()
