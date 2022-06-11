def collatz_conjecture(n: int, steps: int = 0) -> int:
    """
    n: The starting number.

    Returns: the integer count of steps taken until reaching the
    number 1 using the collatz conjecture.
    """
    if n <= 0:
        raise ValueError("Only positive integers are allowed.")

    if n == 1:
        return steps

    if n % 2 == 0:
        return collatz_conjecture(n // 2, steps = steps + 1)
    return collatz_conjecture(n * 3 + 1, steps = steps + 1)


print(f"""Steps taken: {
    collatz_conjecture(
        n=int(
            input("Number to find the collatz conjecture for: ")
        )
    )}""")
