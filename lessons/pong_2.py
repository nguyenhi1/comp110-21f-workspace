"""Pong def function practice"""

CUP: str = '\U0001F964'
SHOT: str = '\U00002716'

from random import randint

def shot():
    shot = randint(1, 3)
    if shot == 1:
        print("", SHOT, "\n", CUP)
    else:
        if shot == 2:
            print("", CUP, "\n", SHOT)
        else:
            print("", CUP, "\n", CUP)


shot()