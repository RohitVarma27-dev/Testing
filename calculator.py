"""Simple calculator functions for practice."""


def add(a, b):
    """Return sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raise on divide-by-zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("20 / 5 =", divide(20, 5))
