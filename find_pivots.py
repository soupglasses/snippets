"""
You are going to be given an array of integers. Your job is to take
that array and find an index N where the sum of the integers to the
left of N is equal to the sum of the integers to the right of N.
If there is no index that would make this happen, return -1.
"""
from typing import Any, Sequence


def pivot(arr: Sequence, pos: int) -> tuple[Sequence, Any, Sequence]:
    """Returns a three part tuple, seperated at the index `pos`.

    Args:
        arr: A sequence of items to pivot on.
        pos: The index where the pivot will be.

    Returns:
        A tuple containing 3 items. First holding all items up to
        the pivot Second is the item at the pivot. Third holding
        all items after the pivot.

    Examples:
        >>> pivot([1,2,3,4,5], 2)
        ([1, 2], 3, [4, 5])
    """
    return arr[:pos], arr[pos], arr[pos + 1 :]


def find_pivot(lst: Sequence) -> int:
    """Finds the lowest pivot where both sides are summed equal.

    Returns:
        The lowest integer index where the sum of the left side of
        `pos` will be equal to the sum of the right side of `pos`.
        If there is no valid index where this is true, return -1.
    """
    for i in range(len(lst)):
        left, _, right = pivot(lst, i)
        if sum(left) == sum(right):
            return i

    return -1


def main():
    test_cases = (
        (0, (15,)),
        (-1, tuple()),
        (3, (1, 2, 3, 4, 3, 2, 1)),
        (1, (1, 100, 50, -51, 1, 1)),
        (0, (20, 10, -80, 10, 10, 15, 35)),
    )
    for answer, data in test_cases:
        print(f"Answer: {answer} is {find_pivot(data)}")


if __name__ == "__main__":
    main()
