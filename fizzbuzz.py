"""Classic FizzBuzz exercise for practice."""


def fizzbuzz(n):
    """Return FizzBuzz string for a single number n."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def run(limit):
    """Print FizzBuzz from 1 to limit."""
    for i in range(1, limit + 1):
        print(fizzbuzz(i))


if __name__ == "__main__":
    run(20)
