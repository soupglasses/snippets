"""
# Global Warming

This is my solution to a task called "Problem J4: Global Warming". It's rather
difficult to solve due to its badly written problem description, and you have
to play around quite a bit with the data to realize what they mean.

If you want to attempt a challenging nut, attempt to solve it yourself before
reading my solution here. It's good experience in figuring out what the answer
is with a badly described problem.

Full text: https://i.imgur.com/ENga7ht.png
"""
from itertools import cycle
from typing import Generator, Union


def linear_sequences(data: list) -> Generator[list, None, None]:
    """
    Returns all possible combinations of linear sequences.

    >>> list(linear_sequences([2,3]))
    [[2], [2, 3], [3]]

    >>> list(linear_sequences([]))
    []
    """
    for offset in range(len(data)):
        for i in range(offset, len(data)):
            yield data[offset : i + 1]


def find_shortest_pattern(data: list) -> list:
    """
    Find the shortest cycle that doesnt inlucde the lowest value if unique.

    1. It cannot start at the lowest unique number.
    2. The ending can show the start of a repeating pattern.
    3. It needs to be the shortest one found.
    4. Needs at minimum 2 inputs in list, otherwise return [].
    5. A cycle will always exist, even if its the full input.

    >>> find_shortest_pattern([1, 2, 1])
    [1, 2]

    >>> find_shortest_pattern([1, 2, -2, 1, 2, -2])
    [1, 2, -2]

    >>> find_shortest_pattern([-4, 1, 2, -2, 1, 2, -2])
    [1, 2, -2]

    >>> find_shortest_pattern([-2, 2, 2])
    [2]

    >>> find_shortest_pattern([-2, 3, 1])
    [3, 1]

    >>> find_shortest_pattern([-1, 1, 2, 1])
    [1, 2]

    >>> find_shortest_pattern([0])
    []
    """
    # We cant find a pattern on a list that is length 0 or 1.
    if len(data) < 2:
        return []

    # Pattern starts after the lowest unique temperature.
    # If there is no unique lowest temperature, we use the full list.
    min_ = min(data)
    if data.count(min_) == 1:
        data = data[data.index(min_) + 1 :]

    # The full list is also a pattern, but the longest.
    answer = data
    for sub_list in linear_sequences(data):
        # Check that the pattern fits our full list.
        if all(a == b for a, b in zip(cycle(sub_list), data)):
            # See if the new pattern is shorter than the current answer.
            if len(sub_list) < len(answer):
                answer = sub_list

    return answer


def global_warming(avg_temps: list) -> Union[int, None]:
    """
    Problem J4: Global Warming

    Produce the length of the shortest temperature cycle. The cycle always
    exists, since the whole sequence could be treated as one long cycle.

    Full task: https://i.imgur.com/ENga7ht.png
    """
    # A cycle needs at least 2 measurements.
    if len(avg_temps) < 2:
        return None

    # The cycle is defined as the temperature change between measurements.
    differences = [current - last for last, current in zip(avg_temps, avg_temps[1:])]

    return len(find_shortest_pattern(differences))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    samples = [
        [3, [3, 4, 6, 4, 5, 7, 5]],
        [2, [3, 4, 6, 7]],
        [3, [7, 3, 4, 6, 4, 5, 7, 5]],
        [1, [3, 1, 3, 5]],
        [2, [3, 1, 4, 5]],
        [None, [0]],
    ]

    for result, data in samples:
        if result != global_warming(data):
            print("Data:", data, "did not result in expected output:", result)
