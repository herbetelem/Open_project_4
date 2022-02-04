import sqlite3

# class who will do the request SQL


class SQL_function():

    # connect the bdd and create the cursor
    def __init__(self):
        self.connector = sqlite3.connect('tournament_checkmate.db')
        self.cursor = self.connector.cursor()

    # get the country from bdd
    def get_country(self):
        self.cursor.execute('SELECT * FROM country')
        result = self.cursor.fetchall()
        return result

    # get the town from bdd
    def get_town(self, country):
        country = (country[0],)
        self.cursor.execute('SELECT * FROM town where id_country = ?', country)
        result = self.cursor.fetchall()
        return result

    # get the place from bdd
    def get_location(self, town):
        town = (town[0],)
        self.cursor.execute('SELECT * FROM location where id_town = ?', town)
        result = self.cursor.fetchall()
        return result

    # create the tournament
    def create_tournament(self, data, players):
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


    def get_players(self, search):
        request = f"SELECT * FROM player WHERE lastname LIKE '%{search}%' LIMIT 8;"
        self.cursor.execute(request)
        result = self.cursor.fetchall()
        return result
