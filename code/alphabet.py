"""
Title: Alphatbet class
Author: Red spotted bittern

Purpose:
    tbc.

Log:
    03.10.2023: Last change
    07.04.2024: Got familiar with the program again.
    09.04.2024: Finished almost all Letters. Würfeln is left.
    09.04.2024: Moved the delta function here.
"""


def delta(gamestate, lexikon):
    # Gamestate: engine
    # Input Alphabet: lexikon
    # Output Alphabet: omegabet

    # Call do_it beim nächsten Buchstaben
    engine, satz, omegabet = lexikon.pop(0).do_it()

    # setze die neuen Buchstaben in die Spitze der Liste
    lexikon = satz + lexikon

    return engine, lexikon, omegabet


class Alphabet():
    def __init__(self, gamestate):
        self.gamestate = gamestate

    def do_it(self):
        print('YO')

    def __repr__(self):
        return str(self.__class__)[17:-2]


class Start(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):

        alphabet = [Würfeln(self.tisch)]

        return self.tisch, alphabet, 'omegabet'


class Würfeln(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):

        # Lass alle einmal würfeln
        # Das hier muss natürlich noch feiner werden
        self.tisch.alle_würfeln()

        alphabet = [Wurfranking(self.tisch)]

        return self.tisch, alphabet, 'omegabet'


class Wurfranking(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):
        # plus immer output alphabet "RANKED"

        # Lass den Tisch die Plätze der Player bestimmen
        self.tisch.wurfranking()

        # Verändere die nächsten Schritte danach, ob Stechen nötig ist
        alphabet = []
        if len(self.tisch['best']) > 1:
            alphabet.append(Stechen(self.tisch, 'best'))
        if len(self.tisch['worst']) > 1:
            alphabet.append(Stechen(self.tisch, 'worst'))

        alphabet.append(Abrechnen(self.tisch))

        return self.tisch, alphabet, 'omegabet'


class Stechen(Alphabet):
    def __init__(self, tisch, mode):
        super().__init__(tisch)
        self.tisch = tisch
        self.mode = mode

    def do_it(self):
        """ Mach einen Stichwurf entsprechend des Modus ob die Besten oder
            Schlechtesten stechen sollen. """

        # Mach Stichwurf entsprechend des Modus (best or worst)
        self.tisch.stechen(self.mode)

        # Wenn das keinen Gewinner hervorgebracht hat, erweitere das Alphabet
        alphabet = []
        if len(self.tisch[self.mode]) > 1:
            alphabet.append(Stechen(self.tisch, self.mode))

        return self.tisch, alphabet, 'omegabet'


class Abrechnen(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):

        # Lass den Tisch die Deckel verteilen
        self.tisch.abrechnen()

        # Übergib an Rauswerfen
        alphabet = [Rauswerfen(self.tisch)]

        return self.tisch, alphabet, 'omegabet'


class Rauswerfen(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):

        # Darf schon rausgeworfen werden? Logisch Teil des Phasenchecker
        if self.tisch.deckel <= 0:
            # check if a player has 0 Bierdeckel and may leave the round
            for player in self.tisch.runde.copy():
                if player.bierdeckel <= 0:
                    self.tisch - player

        alphabet = [Phasenchecker(self.tisch)]

        return self.tisch, alphabet, 'omegabet'


class Phasenchecker(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):
        """ Diese Funktion überprüft nach dem Rauswerfen den Stand der
        Dinge.
        Gibt es nur noch ein Player, werden Punkte abgezogen und das Spiel
        beendet.
        Bei zwei Player wird "head2head" ausgerufen und weitergewürfelt.
        Bei mehr als zwei wird "nostack" ausgerufen und weitergewürfelt.
        """

        assert len(self.tisch.runde) != 0, "something is fishy"

        alphabet = []
        if self.tisch.deckel > 0:
            # Noch in der ersten Phase
            alphabet.append(Würfeln(self.tisch))

        elif len(self.tisch.runde) == 1:
            # Nur noch ein Player übrig
            alphabet.append(Punktabzug(self.tisch))

        elif len(self.tisch.runde) == 2:
            # Es sind nur noch zwei Player übrig
            self.tisch.phase = 'head2head'
            alphabet.append(Würfeln(self.tisch))

        elif self.tisch.deckel <= 0:
            # Der Stack ist aufgebraucht
            self.tisch.phase = 'nostack'
            alphabet.append(Würfeln(self.tisch))

        return self.tisch, alphabet, 'omegabet'


class Punktabzug(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch

    def do_it(self):

        # Let the tisch select the loser
        self.tisch.select_loser()

        alphabet = [Reset(self.tisch)]

        return self.tisch, alphabet, 'omegabet'


class Reset(Alphabet):
    def __init__(self, tisch):
        super().__init__(tisch)
        self.tisch = tisch
        self.mode = haus,tisch

    def do_it(self):

        # Let the tisch reset
        self.tisch.reset()

        alphabet = [Würfeln(self.tisch)]

        return self.tisch, alphabet, 'ENDE'
