"""Repeating a beat in a loop."""

__author__ = "730402537"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
counts: int = 0
number: int = int(input("How many times do you want to repeat it? "))
if number <= 0:
    print("No beat...")
else:
    while counts < number:
        beat_repeat: str = (beat + (" ")) * (number - 1) + (beat)
        print(beat_repeat)
        counts = counts + 1
        counts = counts * number