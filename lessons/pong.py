"""Creating cup pong"""

# from random import randint

CUP: str = '\U0001F964'
# SHOT: str = '\U00002716'

# first_row: str = CUP*4
# print(first_row)
# # print(len(first_row))

# second_row: str = CUP*3
# print("", second_row)
# # print(len(first_row) + len(second_row))

# third_row: str = CUP*2
# print(" ", third_row)
# # print(len(first_row) + len(second_row) + len(third_row))

# fourth_row: str = CUP
# print("  ", fourth_row)
# # print(len(first_row) +len(second_row) + len(third_row) + len(fourth_row))
# # cups: int = (len(first_row) +len(second_row) + len(third_row) + len(fourth_row))
# cups: str = first_row \
#      + second_row \
#      + third_row \
#      + fourth_row
# print(cups)

print(CUP*4, "\n", CUP*3, "\n ", CUP*2, "\n  ", CUP)
total_cups: str = CUP*4 + CUP*3
print(total_cups)