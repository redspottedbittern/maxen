"""
Title: Tisch class
Author: Red spotted bittern

Purpose:
    tbc.

Log:
    03.10.2023: Last change
    07.04.2024: Got familiar with the program again.
    08.04.2024: Made Runde to Tisch and integrated the game

Notes:
    - Good way to do __repr__?
    - Check type for __sub__?
    - coole map für die Runde?
"""

from player import Player
from utils import name_generator


class Tisch():
    def __init__(self, num_player, num_deckel=15):
        self.max_deckel = num_deckel
        self.deckel = num_deckel
        self.leute = self.initialize_players(num_player)
        self.runde = self.leute.copy()
        self.best = []
        self.worst = []
        self.phase = 'yesstack'

    def __str__(self):
        return str([(str(p), p) for p in self.runde])

    def initialize_players(self, num_players):
        """ This takes the number of player and gives each of them a name and
        puts them in a list. """

        names = name_generator(num_players)
        # additionally give deckel, lost_game, total_num_würfel and seiten
        players = [Player(names[n]) for n in range(num_players)]

        return players

    def __getitem__(self, keyword):
        """ Implements accessing best and worst like a dict. """
        if keyword == 'best':
            return self.best
        elif keyword == 'worst':
            return self.worst

    def __setitem__(self, keyword, players):
        """ Implements setting best and worst like a dict. """
        if keyword == 'best':
            self.best = players
        elif keyword == 'worst':
            self.worst = players

    def __sub__(self, player):
        self.runde.remove(player)

    def reset(self):
        self.deckel = self.max_deckel
        self.phase = 'yesstack'
        self.runde = self.leute.copy()
        for player in self.runde:
            player.reset()

    def alle_würfeln(self):
        for player in self.runde:
            player([])

    def wurfranking(self):
        """ Rank the players according to the Wurf and determine best and worst
        players. """

        # Sollen worst und best als Liste oder einzelne gespeichert werden?
        # Game müsste dann ggf. das Wurfranking machen und stechen lassen bis
        # bester und schlechtester feststehen

        ranking = sorted(self.runde, reverse=True)

        self.best = [player for player in ranking if player ==
                     ranking[0].wurf]
        self.worst = [player for player in ranking if player ==
                      ranking[-1].wurf]

    def stechen(self, mode):
        """ This function takes a list of players and performs a Stechen
        between them in not more than three loops! """

        for player in self[mode]:
            player.stich_würfeln()

        if mode == 'best':
            threshold = max([p.get_stichwert() for p in self[mode]])
        elif mode == 'worst':
            threshold = min([p.get_stichwert() for p in self[mode]])

        selected = []
        for player in self[mode]:
            if player.get_stichwert() == threshold:
                selected.append(player)

        self[mode] = selected

    def abrechnen(self):
        """ Verteilen der Bierdeckel am Ende eines Würfeldurchgangs,
        entsprechend der Phase, die im Alphabet bestimmt wird. """

        # test just for safety
        assert len(self.best) == 1 and len(self.worst) == 1, \
            "too many loosers and winners"

        best = self.best[0]
        worst = self.worst[0]
        deckel = best.get_wurfkosten()

        if self.phase == 'head2head':
            # deckel werden in die mitte gespielt
            best - deckel
        elif self.phase == 'nostack':
            # best gibt worst die deckelanzahl
            best - deckel
            worst + deckel
        elif self.phase == 'yesstack':
            # worst bekommt deckel vom stack
            self.deckel -= deckel
            worst + deckel

    def select_loser(self):
        # Test for safety measures
        assert len(self.runde) == 1, "No single loser yet."

        self.runde[0].lose()

    def old_stechen(self, players, mode):
        """ This function takes a list of players and performs a Stechen
        between them in not more than three loops! """

        for player in players:
            player.stich_würfeln()

        if mode == 'best':
            threshold = max([p.get_stichwert() for p in players])
        elif mode == 'worst':
            threshold = min([p.get_stichwert() for p in players])

        selected = []
        for player in players:
            if player.get_stichwert() == threshold:
                selected.append(player)

        return selected

    def old_abrechnen(self, best, worst):
        """ Verteilen der Bierdeckel am Ende eines Würfeldurchgangs """

        # soll hier noch die Phase eingeführt werden oder so?

        deckel = best.get_wurfkosten()

        if len(self.runde) == 2:
            # deckel werden in die mitte gespielt
            best - deckel
        elif self.deckel < 1:
            # best gibt worst die deckelanzahl
            best - deckel
            worst + deckel
        else:
            # worst bekommt deckel vom stack
            self.deckel -= deckel
            worst + deckel
