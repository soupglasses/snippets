from itertools import takewhile
from more_itertools import all_equal, first


def longest_common_prefix(words: list[str]) -> str:
    """
    Finds the longest common prefix string amongst a list of strings.

    Returns an empty string if no common prefix is found.

    >>> longest_common_prefix([])
    ''

    >>> longest_common_prefix(["hello"])
    'hello'

    >>> longest_common_prefix(["hello", "help", "hero"])
    'he'
    """
    return "".join(map(first, takewhile(all_equal, zip(*words))))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for inp in (["hello"], ["travel", "trapped", "transfer"], []):
        print(
            "{!r} is the longest prefix for {!r}".format(
                longest_common_prefix(inp), inp
            )
        )
