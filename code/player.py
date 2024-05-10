"""
Title: A player with a lot of magic methods
Author: Red spotted bittern

Purpose:
    This is the player class that gives them actions!

Log:
    07.04.2024: Got the idea and played around with it. Implemented all
    necessary magic functions and divided the wurf and call.
"""

import random
from utils import init_augen


class Player():
    """ This is the player class. The player stores information about themelves
    and can throw dice. """

    def __init__(self, name, bierdeckel=0, lost_games=0,
                 total_num_würfel=3, seiten=6):
        self.augen, self.augen2bierdeckel = init_augen()
        self.name = name
        self.bierdeckel = bierdeckel
        self.lost_games = lost_games
        self.wurf = []
        self.stichwurf = []
        self.total_num_würfel = total_num_würfel
        self.seiten = list(range(1, seiten+1))

    def lose(self):
        self.lost_games += 1

    def __add__(self, bierdeckel):
        self.bierdeckel += bierdeckel

    def __sub__(self, bierdeckel):
        self.bierdeckel -= bierdeckel

    def reset(self):
        # self.wurf = []
        self.bierdeckel = 0

    def get_wurfkosten(self):
        return self.augen2bierdeckel[str(self.wurf)]

    def get_stichwert(self):
        return sum(self.stichwurf)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.wurf)

    def __getitem__(self, idx):
        """ Implements accessing single numbers. """
        return self.wurf[idx]

    def __setitem__(self, idx, item):
        # do I need this?
        """ Implements setting single numbers. """
        self.wurf[idx] = item
        self.wurf.sort(reverse=True)

    def __lt__(self, wurf):
        return self.augen.index(self.wurf) > self.augen.index(wurf)

    def __gt__(self, wurf):
        return self.augen.index(self.wurf) < self.augen.index(wurf)

    def __eq__(self, wurf):
        return self.augen.index(self.wurf) == self.augen.index(wurf)

    def __ne__(self, wurf):
        return self.augen.index(self.wurf) != self.augen.index(wurf)

    def __call__(self, wurf):
        """ Macht einen Wurf und speichert ihn, wenn man die Klasse direkt
        aufruft. """
        self.wurf = self.würfeln(wurf)

    def würfeln(self, wurf):
        """ Nimmt eine Liste an Zahlen und fügt dieser solange Zahlen der
        self.seiten hinzu bis es total_num_würfel sind. """

        for num in range(self.total_num_würfel - len(wurf)):
            wurf.append(random.choice(self.seiten))

        wurf.sort(reverse=True)

        return wurf

    def stich_würfeln(self):
        self.stichwurf = self.würfeln([])

    def six2one(self, drei6=False):
        """ Transformiert zwei oder drei 6er zu einer oder zwei 1er """

        if len(self.wurf) == 3 and self.wurf.count(6) > 1:
            if drei6:
                self.wurf = [1, 1]
            else:
                self.wurf = [self.wurf[2], 1]
        # maybe + würfeln?
