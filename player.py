import random

class Player:

    def __init__(self,id_player , name, last_name, global_rank, score=0):
        """ Object player

        Args:
            id_player (int): the id of the player
            name (str): the name of the player
            last_name (str): the lastname of the player
            global_rank (int): the global rank of the player
            score (int, optional): the score of the player. Defaults to 0.
        """
        
        self.id = id_player
        self.name = name
        self.last_name = last_name
        self.global_rank = global_rank
        self.score = score
        self.matched = []
        self.choosed = False
        self.pool = 0
        self.pool_rank = 0