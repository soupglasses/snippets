"""
# Spongebob text generator

Playing around with functional over imperative apporaches to
programming. This example uses the Mocking Spongebob meme[1]
as an inspiration. Where text will cycle between lower- and
upper-case for each letter.

It will also ignore non letters and spaces for this cycle,
making the input of `"a b"` become `"A b"` and not `"A B"`.

Output:
```
Functional: TeStInG! dOeSn'T tHiS lOoK gRe8T?
Imperative: TeStInG! dOeSn'T tHiS lOoK gRe8T?
```

1: https://knowyourmeme.com/memes/mocking-spongebob
"""
from itertools import cycle
from typing import Iterable

from more_itertools import partition


def cycle_case(iterable: Iterable) -> Iterable:
    return zip(cycle((str.upper, str.lower)), iterable)


def spongebob_functional(text: str) -> str:
    not_letters, letters = partition(str.isalpha, text)
    cased_letters = (func(letter) for func, letter in cycle_case(letters))

    return "".join(
        next(cased_letters) if letter.isalpha() else next(not_letters)
        for letter in text
    )


def spongebob_imperative(text: str) -> str:
    letters = []
    pos = 0
    for letter in text:
        if letter.isalpha():
            if pos % 2 == 0:
                letters.append(letter.upper())
            else:
                letters.append(letter.lower())
            pos += 1
        else:
            letters.append(letter)
    return "".join(letters)


if __name__ == "__main__":
    EXAMPLE_TEXT = "Testing! Doesn't this look gre8t?"
    print("Functional:", spongebob_functional(EXAMPLE_TEXT))
    print("Imperative:", spongebob_imperative(EXAMPLE_TEXT))
