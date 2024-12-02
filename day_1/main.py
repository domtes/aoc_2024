import bisect
from collections import Counter
from typing import Generator, TextIO, Tuple


def read_input(f: TextIO) -> Generator[Tuple[int, int], None, None]:
    for line in f:
        x, y = line.strip().split()
        yield (int(x), int(y))


def total_distance() -> int:
    left = []
    right = []
    total_distance = 0

    with open("input.txt", "r") as f:
        for x, y in read_input(f):
            bisect.insort(left, x)
            bisect.insort(right, y)

    for x, y in zip(left, right):
        total_distance += abs(x - y)

    return total_distance


def similarity_score() -> int:
    left = []
    right = []
    similarity_score = 0

    with open("input.txt", "r") as f:
        for x, y in read_input(f):
            left.append(x)
            right.append(y)

    frequencies = Counter(right)

    for x in left:
        similarity_score += x * frequencies[x]

    return similarity_score


if __name__ == "__main__":
    print(f"total_distance = {total_distance()}")
    print(f"similarity_score = {similarity_score()}")
