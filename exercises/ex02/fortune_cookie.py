"""Program that outputs one of at least four random, good fortunes."""

__author__ = "370402537"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune = randint(1, 4)
if fortune == 1:
    print("Your generous COMP-110 professor will give you a free 100 exam grade.")
else:
    if fortune == 2:
        print("Soon, you will be able to create a code that tells fortunes.")
    else:
        if fortune == 3:
            print("A loyal companion will soon join your life... go adopt a dog.")
        else:
            print("The autograder will find nothing wrong with your code")

print("Now, go spread positive vibes!")