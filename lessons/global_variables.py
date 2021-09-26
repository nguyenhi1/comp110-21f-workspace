"""Practice for global variables"""


def name():
    global player
    player = input("Enter your name: ")
    print("\n")
    print("Welcome", (player), "have fun.")

name()