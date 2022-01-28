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
    def create_tournament(self, data):
        new_tournament = (self.cursor.lastrowid,
        data[0],
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6],)
        import pdb; pdb.set_trace()
        self.cursor.execute('INSERT INTO tournament VALUES(?,?,?,?,?,?,?,?)', new_tournament)
        self.connector.commit()
