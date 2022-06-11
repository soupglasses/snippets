"""
# Cup Ballet

My answer for the cup ballet question.
https://imgur.com/Vqc4p5o

Example Input:
    4
    4
    0 1
    2 3
    3 0
    1 2

Example Output:
    1

"""


def fetch_from_file(file: str) -> dict:
    with open(file) as f:
        raw_data = f.read().splitlines()

    cups = int(raw_data.pop(0))
    total_swaps = int(raw_data.pop(0))

    swaps = []
    for line in raw_data:
        swap = tuple(map(int, line.split(" ")))
        swaps.append(swap)

    data = {"cups": cups, "total_swaps": total_swaps, "swaps": swaps}

    return data


def fetch_from_input() -> dict:
    cups = int(input())
    total_swaps = int(input())

    swaps = []
    for _ in range(total_swaps):
        swap = tuple(map(int, input().split(" ")))
        swaps.append(swap)

    data = {"cups": cups, "total_swaps": total_swaps, "swaps": swaps}

    return data


def cup_ballet(cups: int, swaps: list[tuple[int, int]]) -> int:
    table = [" " for _ in range(cups - 1)] + ["O"]

    for left, right in swaps:
        table[left], table[right] = table[right], table[left]

    return table.index("O")


if __name__ == "__main__":
    data = fetch_from_file("data.txt")

    ball_pos = cup_ballet(cups=data["cups"], swaps=data["swaps"])
    print(ball_pos)
