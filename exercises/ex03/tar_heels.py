"""An exercise in remainders and boolean logic."""

__author__ = "730402537"


# Begin your solution here...
num: int = int(input("Enter an int: "))
if num % 2 == 0:
    if num % 7 == 0:
        print ("TAR HEELS")
    else:
        print ("TAR")
else:
    if num % 7 == 0:
        print ("HEELS")
    else:
        print ("CAROLINA")