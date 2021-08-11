"""
# Histogram

Creates a printable histogram based on the inputted list of numbers.

Output:
```
0   | *
10  | ****
20  | *****
30  | ********
40  | **********
50  | **********
60  | ******
70  | ******
80  | *****
90  | ****
100 | *
```
"""
from collections import Counter, defaultdict


def histogram(data: list[int], *, step: int = 10, limit: int = 100) -> str:
    """
    Create a printable histogram based on the inputted list of values.

    Example Output:
        0   | *
        10  | ****
        20  | *****
    """
    counts = Counter(data)
    groups = defaultdict(int)

    for number, count in counts.items():
        if number > limit:
            continue
        groups[number - number % step] += count

    return "\n".join(
        [f"{group:<3} | {'*' * count}" for group, count in sorted(groups.items())]
    )


if __name__ == "__main__":
    # fmt: off
    data = [
        14, 45, 78, 89, 23,
        12, 52, 43, 14, 76,
        87, 88, 87, 76, 76,
        90, 99, 100, 23, 32,
        41, 20, 45, 54, 52,
        67, 89, 43, 21, 43,
        56, 67, 67, 78, 59,
        93, 33, 11, 1, 43,
        55, 45, 67, 65, 54,
        76, 67, 59, 95, 20,
        34, 32, 37, 38, 30,
        30, 45, 56, 56, 45,
    ]
    # fmt: on
    print(histogram(data))
