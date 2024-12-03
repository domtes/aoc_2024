import re
from collections import namedtuple
from typing import Generator, List, TextIO


Mul = namedtuple("Mul", ["x", "y"])
MulPattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
ExtendedPattern = re.compile(r"(?P<op_mul>mul)\((\d{1,3}),(\d{1,3})\)|(?P<op_do>do)\(\)|(?P<op_dont>don't)\(\)")


def parse_mul_ops(f: TextIO) -> List[Mul]:
    input_string = f.read()
    return [Mul(int(x), int(y)) for x, y in MulPattern.findall(input_string)]

def parse_mul_ops_extended(f: TextIO) -> Generator[Mul, None, None]:
    input_string = f.read()

    mul_enabled = True
    for match in ExtendedPattern.finditer(input_string):

        if match.group("op_dont"):
            mul_enabled = False
        elif match.group("op_do"):
            mul_enabled = True

        if match.group("op_mul") and mul_enabled:
            yield Mul(int(match.group(2)), int(match.group(3)))


def main():
    input_file = "input.txt"

    total = 0
    total_extended = 0
    with open(input_file, "r") as f:
        for x, y in parse_mul_ops(f):
            print(f"mul({x}, {y}) = {x * y}")
            total += x * y

    with open(input_file, "r") as f:
        for x, y in parse_mul_ops_extended(f):
            print(f"mul({x}, {y}) = {x * y}")
            total_extended += x * y

    print(f"total = {total}")
    print(f"total_extended = {total_extended}")


if __name__ == "__main__":
    main()
