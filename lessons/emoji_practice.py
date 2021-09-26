"""Trying out bucket emoji"""

from random import randint

CUP: str = '\U0001F964'
SHOT: str = '\U00002716'

cups = 4
space = 0
total_cups = 0
while cups <= 4 and cups > 0:
    print(" "*space, (CUP)*cups)
    total_cups: int = cups + total_cups
    assigned_cups: str = CUP*cups
    cups = cups - 1 
    space = space + 1

# i: int = 0
# count: int = 0
# while i < 10:


# shot = randint(1, 3)
# if shot == 1:

# shot = randint(1,3)
# if shot == 1:
#     print(SHOT)
#     print(CUP)
# else:
#     if shot == 2:
#         print(CUP)
#         print(SHOT)
#     else:
#         print(CUP)
#         print(CUP)