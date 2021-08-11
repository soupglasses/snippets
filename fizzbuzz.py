"""
# Fizz buzz

Example of how to implement fizz buzz[1] in Python.

[1]: https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz(num: int) -> str:
    return "Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0) or str(num)


if __name__ == "__main__":
    print(", ".join(fizzbuzz(i) for i in range(1, 101)))
