from typing import List, TextIO


def read_input(f: TextIO) -> List[int]:
    for line in f:
        yield [int(n) for n in line.strip().split()]


def is_safe(report: List[int]) -> bool:
    increasing = True
    for j in range(0, len(report)):
        n1, n2 = report[j], report[j + 1]

        if n1 == n2:
            return False

        increasing = n2 > n1
        break

    for j in range(0, len(report)):
        if j == len(report) - 1:
            break

        n1, n2 = report[j], report[j + 1]
        if n1 == n2:
            return False
        if increasing and n1 > n2:
            return False
        if not increasing and n1 < n2:
            return False

        if 1 < abs(n2 - n1) > 3:
            return False

    return True


def count_safe_reports(f: TextIO) -> int:
    total = 0
    for report in read_input(f):
        safe = is_safe(report)

        if safe:
            total += 1

    return total


def count_safe_reports_with_tolerance(f: TextIO) -> int:
    total = 0
    for report in read_input(f):
        safe = is_safe(report)

        if not safe:
            for n in range(1, len(report) + 1):
                safe = is_safe(report[0 : n - 1] + report[n:])
                if safe:
                    break

        if safe:
            total += 1

    return total


def main():
    input_file = "input.txt"

    with open(input_file, "r") as f:
        print(f"safe_reports = {count_safe_reports(f)}")

    with open(input_file, "r") as f:
        print(f"safe_reports_with_tolerance = {count_safe_reports_with_tolerance(f)}")


if __name__ == "__main__":
    main()
