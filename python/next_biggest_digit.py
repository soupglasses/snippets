"""
Next bigger number with the same digits

Task from: https://www.codewars.com/kata/55983863da40caa2c900004e
"""


def smallest(text: str) -> str:
    "Returns the smallest string possible using unicode code points"
    return "".join(sorted(text))


def biggest(text: str) -> str:
    "Returns the biggest string possible using unicode code points"
    return "".join(sorted(text, reverse=True))


def swap(a: str, l: int, r: int) -> str:
    "Returns a string with swapped characters at l and r"
    return a[0:l] + a[r] + a[l + 1 : r] + a[l] + a[r + 1 :]


def next_bigger(num: int) -> int:
    """
    Returns the next bigger number that can be formed by rearranging digits.

    Takes only a positive integer.

    Algorithm:
        1. Go right-to-left, compare against window's biggest num. Take first
        window which is not equal.
        2. Find next biggest digit to the leftmost digit, swap leftmost digit
        and next biggest digit using a left-to-right priority.
        3. Take right hand side without leftmost digit, create its smallest
        number.

    Tests:
        >>> next_bigger(12)
        21

        >>> next_bigger(21)
        -1

        >>> next_bigger(2017)
        2071

        >>> next_bigger(646551)
        651456
    """
    number = str(num)
    rtl_windows = [
        (number[:pos], number[pos:]) for pos in range(len(number) - 2, -1, -1)
    ]
    for lhs, rhs in rtl_windows:
        if biggest(rhs) > rhs:  # 1.
            next_biggest_digit = next(n for n in smallest(rhs[1:]) if n > rhs[0])
            rhs = swap(rhs, 0, rhs.index(next_biggest_digit))  # 2.
            rhs = rhs[0] + smallest(rhs[1:])  # 3.
            return int(lhs + rhs)
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
