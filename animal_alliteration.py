from random import choice
from typing import List

__author__ = 'Markus - elec3647'

alpha: str = 'abcdefghijklmnopqrstuvwxyz'

with open('adjectives.txt') as adj:
    with open('animals.txt') as ani:
        adjectives: List[str] = adj.readlines()
        animals: List[str] = ani.readlines()
        letter = choice(alpha)
        reg1: List[str] = [line.strip() for line in adjectives if letter == line[0].lower()]
        reg2: List[str] = [line.strip() for line in animals if letter == line[0].lower()]
        if len(reg1) == 0 or len(reg2) == 0:
            pass
        else:
            completed_string: str = '%s %s' % (choice(reg1), choice(reg2))
            print(completed_string.title())
