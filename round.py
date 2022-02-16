from calendar import c
from cgitb import reset
from datetime import datetime
from multiprocessing import pool
from pickle import FALSE
from re import A
from secrets import randbelow
from SQL_function import SQL_function
from player import Player


# create class round


class Round:

    def __init__(self, players, id_tournament):
        """ Class to manage the round

        Args:
            players (list): list of all players by id
            id_tournament (int): the id of the tournament
        """

        self.name = ""
        self.sql = SQL_function()
        self.players = []
        self.date_start = [0, 0, 0, 0, 0, 0, 0]
        self.date_end = [0, 0, 0, 0, 0, 0, 0]
        self.hour_start = [0, 0, 0, 0, 0, 0, 0]
        self.hour_end = [0, 0, 0, 0, 0, 0, 0]
        self.id_tournament = id_tournament
        self.match = [[1, 2, False], [3, 4, False],
                      [5, 6, False], [7, 8, False]]
        self.match_done = []
        self.nb_turn = 0
        players = self.get_players_info(players)
        for player in players:
            self.players.append(
                Player(player[0], player[2], player[1], player[3]))
        self.settings = False

    def get_players_info(self, players):
        """ method to get the players information about their global_rankd

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

        self.name = f"Round: {self.nb_turn+1}"
        index_match = 0
        self.date_start[self.nb_turn] = datetime.now().strftime('%Y-%m-%d')
        self.hour_start[self.nb_turn] = datetime.now().strftime('%H-%M')
        self.match = [[1, 2, False], [3, 4, False],
                      [5, 6, False], [7, 8, False]]
        self.sort_by_rank()
        # set up all false cause for the new round no one have an adv for now
        list_adv = [False, False, False, False, False, False, False, False]
        list_order = [4, 5, 6, 7, 3, 2, 1, 0]
        for player in self.players:
            is_player_choosed = False
            for match in self.match:
                if player in match:
                    is_player_choosed = True

            if not is_player_choosed and index_match < 4:
                found = False
                for order in list_order:
                    if self.players[order] not in player.matched and not list_adv[order] and not found:
                        self.match[index_match][0] = player
                        self.match[index_match][1] = self.players[order]
                        list_adv[order] = True
                        is_player_choosed = True
                        found = True
                index_match += 1

    def validate_round(self, results):
        """ Method to save the match

        Args:
            results (list): list of result of the match
        """

        score = {
            3: [1, 1],
            1: [2, 0],
            2: [0, 2],
        }
        self.date_end[self.nb_turn] = datetime.now().strftime('%Y-%m-%d')
        self.hour_end[self.nb_turn] = datetime.now().strftime('%H-%M')
        for match in self.match:
            self.sql.save_round((self.id_tournament, match[0].id, match[1].id, match[2], self.name, self.date_start[self.nb_turn],
                                self.date_end[self.nb_turn], self.hour_start[self.nb_turn], self.hour_end[self.nb_turn]))
        for index in range(4):
            # attribution of score
            self.match[index][0].score += score[results[index]][0]
            self.match[index][1].score += score[results[index]][1]

            # add in the history of player their match
            self.match[index][0].matched.append(self.match[index][1])
            self.match[index][1].matched.append(self.match[index][0])
        self.match = [[1, 2, False], [3, 4, False],
                      [5, 6, False], [7, 8, False]]
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
        self.players.sort(key=lambda x: (
            x.score, -x.global_rank), reverse=True)
        for i in range(8):
            self.players[i].pool_rank = i


# item = Round([301, 302, 303, 304, 205, 306, 208, 308])
# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.generate_round()
# item.validate_round([1,3,2,1])

# item.print_score()
