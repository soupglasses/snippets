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
from more_itertools import map_if


class Cycle:
    def __init__(self, *functions):
        self.iterable = cycle(functions)

    def __call__(self, *args, **kwargs):
        return next(self.iterable)(*args, **kwargs)


def spongebob_functional(text: str) -> str:
    return "".join(map_if(text, pred=str.isalpha, func=Cycle(str.upper, str.lower)))


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
    example_text = "Testing! Doesn't this look gre8t?"
    print("Functional:", spongebob_functional(example_text))
    print("Imperative:", spongebob_imperative(example_text))
