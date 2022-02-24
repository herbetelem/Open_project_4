import random
import sqlite3

# Test file who is here to generate random player into the database

name_male = ["percy", "grover", "thesee",  "mathieu",
             "jason", "eliotte",  "tom",
             "nico", "lisa", "marriane",
             "sasha", "maurice", "marc", "vincent", "theo", "pierre",
             "eric", "justin",  "laurent", "antoine", "franck",
             "francis",  "marin", ]

name_female = ["annabeth", "julie", "manon", "gabrielle", "marie", "isaure", "thalia",
               "therese", "justine", "amelie", "maud", "pauline", "lea", "rachel", "anna", "calypso",
               "marine", "lucie", "lilliane", "sonia", "sirene"]

firstname = ["martin", "bernard", "thomas", "petit", "durant", "moreau",
             "laurent", "simon", "leroy", "roux", "david", "girard", "lambert", "muller",
             "lefevre", "boyer", "lefevre", "faure", "garnier", "chevalier", "francois",
             "legrand", "gauthier", "garcia", "perrin", "lopez", "jean", "dupuy", "hubert",
             "carpentier", "sanchez", "louis", "fleury", "royer", "klein", "poirier", "carre",
             "menard", "bertin", "herve", "schneider", "legall", "coller"]

list_rank = []


def check_rank(rank):
    my_name = (rank,)
    cursor.execute(
        'SELECT COUNT(*) FROM player WHERE global_rank = ?', my_name)
    result = cursor.fetchone()
    return "ok" if result[0] > 0 else "ko"


def check_name(name, firstname):
    my_name = (name, firstname,)
    cursor.execute(
        'SELECT COUNT(*) FROM player WHERE firstname = ? AND lastname = ?', my_name)
    result = cursor.fetchone()
    return "ok" if result[0] > 0 else "ko"


for i in range(300):
    connector = sqlite3.connect('tournament_checkmate.db')
    cursor = connector.cursor()
    if random.randint(1, 2) == 1:
        tmp_name = random.choice(name_male).capitalize()
        sexe = 1
    else:
        tmp_name = random.choice(name_female).capitalize()
        sexe = 2
    tmp_firstname = random.choice(firstname).capitalize()
    birth = random.randint(1970, 2010)
    rank = random.randint(1, 1500)
    while list_rank.count(rank) > 0:
        rank = random.randint(1, 1500)
    if random.randint(1, 20) == 3:
        sexe = 3
    list_rank.append(rank)

    new_player = (cursor.lastrowid, tmp_name, tmp_firstname, birth, sexe, rank)
    print(new_player)
    cursor.execute('INSERT INTO player VALUES(?,?,?,?,?,?)', new_player)
    connector.commit()
    connector.close()
