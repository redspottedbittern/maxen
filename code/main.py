"""
Title: Main function for the Maxen game
Author: Red spotted bittern

Purpose:
    tbc.

Log:
    15.06.2023: Last change
    07.04.2024: Got familiar with the program again.
    09.04.2024: Finished the Input Alphabet (without human input) and delta

ToDos:
    - Implement Output Alphabet (?)
    - Test more if everything is alright
    - Implement Human Input & finish Würfeln
    - Implement argparse

Options:
    - normales Spiel oder besondere Eingestellungen?
    - Wie viele Player?
    - An welcher Stelle sitzt du?
"""


from tisch import Tisch
from alphabet import Start, delta


def main(num_players):

    engine = Tisch(num_players)
    lexikon = [Start(engine)]
    omegabet = ''

    while omegabet != 'ENDE':
        engine, lexikon, omegabet = delta(engine, lexikon)

        print(lexikon)

    print(engine)
    print(engine.deckel)
    print(omegabet)
