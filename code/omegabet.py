"""
Title: Omegabet - Output Alphabet.

Author: Red-spotted Bittern
Purpose:
    tbc.

Log:
    21.05.2024: Created the first draft of the omegabet.
"""


class Omegabet():
    def __init__(self, gamestate):
        self.gamestate = gamestate

    def __repr__(self):
        return str(self.__class__)[17:-2]


class Gestartet(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print(f"""Spiel ist gestartet mit {len(self.tisch.runde)} Spieler*innen.
              Es spielen:""")
        for player in self.tisch.runde:
            print(player, end=', ')


class Gewürfelt(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print("\n-----------------------------------")
        print("\nAlle Spieler*innen haben gewürfelt:")
        for player in self.tisch.runde:
            print(player, player.wurf, end=', ')


class Geranked(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print("\n\nDen besten Wurf hat", self.tisch.best[0],
              "den schlechtesten hat", self.tisch.worst[0], ".")


class Gestochen(Omegabet):
    def __init__(self, tisch, mode):
        super().__init__(tisch)
        self.tisch = tisch
        self.mode = mode

    def inform(self):
        print(f"""\nEs gibt ein Stechen für {self.mode}""")
        for player in self.tisch[self.mode]:
            print(player.stichwurf)


class Gerechnet(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print("""\nBierdeckel werden verteilt:""")
        for player in self.tisch.runde:
            print(player, player.bierdeckel, end=', ')


class Geworfen(Omegabet):
    def __init__(self, tisch, sind_raus):
        super().__init__(tisch)
        self.tisch = tisch
        self.sind_raus = sind_raus

    def inform(self):
        if len(self.sind_raus) > 0:
            print("""\nEin*e Spieler*in wird rausgeworfen:""")
            for player in self.sind_raus:
                print(player)


class Gechecked(Omegabet):
    def __init__(self, tisch, changed):
        super().__init__(tisch)
        self.tisch = tisch
        self.changed = changed

    def inform(self):
        if self.changed:
            print(f"""\nDas Spiel ist jetzt in dieser Phase: {self.tisch.phase}""")


class Geabzogen(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print(f"""\n{self.tisch.runde[0]} hat das Spiel verloren.""")


class ENDE(Omegabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def inform(self):
        print("""\nDie Runde ist zu Ende.""")
        print(self)
