"""
Title: Utils functions
Author: Red spotted bittern

Purpose:
    tbc.

Log:
    15.06.2023: Last change
    07.04.2024: Got familiar with the program again.
    07.04.2024: Build a random name generator.
"""

import random


def init_augen():
    """ Initiiert die sortierte Liste aller möglichen Würfe"""

    # Liste und Dictionary
    augen = []
    deckelwert = {}

    # generiere alle möglichen Würfe
    zahl = [num for num in range(1, 7)]
    for w1 in zahl:
        for w2 in zahl:
            for w3 in zahl:
                if w1 >= w2 >= w3:
                    augen.append([w1, w2, w3])
                    # augen.append(str(w1) + str(w2) + str(w3))
                    deckelwert[str([w1, w2, w3])] = 1

    for wurf in augen.copy():  # setze straßen nach hinten
        if wurf[0] == wurf[1] + 1 and wurf[1] == wurf[2] + 1:
            augen.remove(wurf)
            augen.append(wurf)
            deckelwert[str(wurf)] = 2

    for wurf in augen.copy():  # setze harte nach hinten
        if wurf[0] == wurf[1] == wurf[2]:
            augen.remove(wurf)
            augen.append(wurf)
            deckelwert[str(wurf)] = 3

    for wurf in augen.copy():  # setze maxe nach hinten
        if wurf[1] == wurf[2] == 1:
            augen.remove(wurf)
            augen.append(wurf)
            deckelwert[str(wurf)] = wurf[0]

    # setze jule und general nach hinten
    augen.remove([4, 2, 1])
    augen.append([4, 2, 1])
    deckelwert['[4, 2, 1]'] = 7
    augen.remove([1, 1, 1])
    augen.append([1, 1, 1])
    deckelwert['[1, 1, 1]'] = 100

    # for idx in range(len(augen)):
    #     wurf = augen[idx]
    #     augen[idx] = int(str(wurf[0]) + str(wurf[1]) + str(wurf[2]))

    augen.reverse()

    return augen, deckelwert


def name_generator(num_names):
    """ This function returns as many names as specified. """

    names = ["Elena", "Max", "Sophia", "Jackson", "Isabella", "Liam", "Ava",
             "William", "Emma", "Oliver", "Mia", "James", "Charlotte",
             "Alexander", "Amelia"]

    players = []
    for idx in range(num_names):
        players.append(random.choice(names))

    return players
