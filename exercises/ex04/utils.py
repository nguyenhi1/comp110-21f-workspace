"""List utility functions."""

__author__ = "730402537"


# TODO: Implement your functions here.
def main() -> None:
    """Entrypoint of program."""
    numbers: list[int] = [1, 1, 1]
    numbers_2: list[int] = [1, 1, 1]
    max_list: list[int] = [1, 1, 1]
    print(all(numbers, 1))
    print(is_equal(numbers, numbers_2))
    print(max(max_list))


def all(numbers: list[int], given: int) -> bool: # This has the red squiggly line beccause it doesn't have return value yet
    i: int = 0
    dups: int = 0
    while i < len(numbers):
        item: int = numbers[i]
        if item == given:
            dups += 1
            i += 1
            if dups == len(numbers):
                return True
        else:
            return False
    return False


def is_equal(numbers: list[int], numbers_2: list[int]) -> bool:
    x: int = 0
    y: int = 0
    dups: int = 0
    while x < len(numbers):
        item: int = numbers[x]
        item_2: int = numbers_2[y]
        if item == item_2:
            dups += 1
            x += 1
            y += 1
            if dups == len(numbers) or dups == len(numbers_2):
                if x == len(numbers) and y == len(numbers_2):
                    return True
                else:
                    return False
        else:
            return False
    return False


def max(max_list: list[int]) -> int:
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
       i: int = 0
       j: int = i + 1
       while i < len(max_list):
            # x: int = 0
            value: int = max_list[i]
            value_2: int = max_list[j]
            if value > value_2:
                if j == len(max_list) - 1:
                    return max_list[i]
                else:
                    j += 1
            else:
                i: int = j
                j += 1
                if j == len(max_list):
                    return max_list[i]
    return max_list[i]


if __name__ == "__main__":
    main()