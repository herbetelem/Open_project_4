import sqlite3
from turtle import pd

# class who will do the request SQL


class SQL_function():

    def __init__(self):
        """ Object who will mannage the SQL request """

        self.connector = sqlite3.connect('annexe/tournament_checkmate.db')
        self.cursor = self.connector.cursor()

    def get_country(self):
        """ Method for getting all the country 

        Returns:
            list: list of all country
        """

        self.cursor.execute('SELECT * FROM country')
        result = self.cursor.fetchall()
        return result

    def get_town(self, country):
        """ Method to get the town of the country selected

        Args:
            country (str): the country selected on the prev step

        Returns:
            list: list of all town in the country selected
        """

        country = (country[0],)
        self.cursor.execute('SELECT * FROM town where id_country = ?', country)
        result = self.cursor.fetchall()
        return result

    def get_location(self, town):
        """ Method for get the location of a town

        Args:
            town (str): the town selected on the prev step

        Returns:
            list: all location of the town
        """

        town = (town[0],)
        self.cursor.execute('SELECT * FROM location where id_town = ?', town)
        result = self.cursor.fetchall()
        return result

    def create_tournament(self, data, players):
        """ Method for save the tournament in bdd

        Args:
            data (list): list of all the tournament data
            players (list): list of all players
        """

        self.cursor.execute('SELECT id FROM tournament')
        result = self.cursor.fetchall()
        if len(result) > 0:
            id_tournament = len(result) - 1
            id_tournament = result[id_tournament][0]
            id_tournament += 1
        else:
            id_tournament = 0
        new_tournament = (id_tournament,
                          data[0],
                          data[1],
                          data[2],
                          data[3],
                          data[4],
                          data[5],)
        self.cursor.execute(
            'INSERT INTO tournament VALUES(?,?,?,?,?,?,?)', new_tournament)
        self.connector.commit()
        for player in players:
            tmp = (id_tournament, player,)
            self.cursor.execute(
                'INSERT INTO player_tournament VALUES(?,?)', tmp)
            self.connector.commit()

    def get_tournament_id(self, data):
        """Method to get the id of a tournament

        Args:
            data (list): list of the data who will be used for the search

        Returns:
            list: result of the search
        """

        request = f"SELECT id FROM tournament WHERE name='{data[0]}' AND description='{data[1]}' AND date='{data[2]}';"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return result

    def get_players(self, search):
        """ Method to get player

        Args:
            search (str): the piece of name from which we will start our search

        Returns:
            list: a list of max 8 name who look likes the search
        """

        request = f"SELECT * FROM player WHERE lastname LIKE '{search}%' LIMIT 8;"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return result

    def get_players_rank(self, players):
        """ Method to get the ranked of the players order by the best

        Args:
            players (list): list of the players

        Returns:
            list: list of the players, order by their global rank
        """

        request = "SELECT id, name, lastname, global_rank FROM player WHERE"
        for player in players:
            request = request + f" id={player} OR"
        request = request[:-3] + " ORDER BY global_rank;"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return result

    def save_round(self, data):
        """ Method to create the round

        Args:
            data (list): list of the data to reccord
        """

        self.cursor.execute(
            'INSERT INTO round VALUES(?,?,?,?,?,?,?,?,?)', data)
        self.connector.commit()

    
    def save_score(self, data):
        """ Method to create the round

        Args:
            data (list): list of the data to reccord (player_id, tournament_id, score)
        """

        self.cursor.execute(
            'INSERT INTO score VALUES(?,?,?)', data)
        self.connector.commit()

    def get_prev_tournament(self):
        """ Method for getting all the tournament who have been done 

        Returns:
            list: list of all tournament done
        """

        self.cursor.execute('SELECT tournament_id FROM score GROUP BY tournament_id;')
        result = self.cursor.fetchall()
        results = []
        for index in result:
            self.cursor.execute(f"SELECT id, name, date FROM tournament WHERE id={index[0]} ORDER BY id DESC LIMIT 6;")
            results.append(self.cursor.fetchall())
        return results

    def get_players_score(self, id_tournament):
        """ Method to get the name lastname and score of a player from a tournament

        Args:
            id_tournament (int): id of the tournament

        Returns:
            list: list of data
        """

        self.cursor.execute(f"SELECT name, lastname, score FROM score INNER JOIN player ON score.player_id = player.id WHERE tournament_id = {id_tournament}")
        result = self.cursor.fetchall()
        return result
