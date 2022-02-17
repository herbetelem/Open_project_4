import pygame
import math


class Tournament:

    def __init__(self):
        """ Object that will keep the data about the tournament """

        self.name = ""
        self.country = ""
        self.town = ""
        self.location = ""
        self.date = ""
        self.nb_turn = 4
        self.nb_tour = ""
        self.players = []
        self.time = ""
        self.description = ""
        self.created = False
        self.id = 0
