"""Drawing forests in a loop."""

__author__ = "730402537"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

if depth == 0:
    pass
else:
    trees: int = 0
    while trees <= depth:
        print(TREE * trees)
        trees += 1