"""Finding duplicate letters in a word."""

__author__ = "730402537"

word: str = input("Enter a word: ")

i: int = 0
while i < len(word):
    char = word[i]
    j: int = i + 1
    while j < len(word):
        char_2 = word[j]
        if char_2 == char:
            print("Found duplicate: True")
            j = j * len(word)
            i = i + len(word)
        else:
            if i == (len(word) - 2):
                print("Found duplicate: False")
                i = i * len(word)
            else:
                j += 1
    i += 1