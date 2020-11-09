from random import choice
__author__ = 'Markus - elec3647'

alpha = 'abcdefghijklmnopqrstuvwxyz'

with open('adjectives.txt') as adj:
    with open('animals.txt') as ani:
        adjectives = adj.readlines()
        animals = ani.readlines()
        letter = choice(alpha)
        reg1 = [line.strip() for line in adjectives if letter == line[0].lower()]
        reg2 = [line.strip() for line in animals if letter == line[0].lower()]
        if len(reg1) == 0 or len(reg2) == 0:
            pass
        else:
            boo ='%s %s' % (choice(reg1), choice(reg2))
            print(boo.title())

