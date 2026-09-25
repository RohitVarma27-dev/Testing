"""List operation helpers for git practice."""


def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9, 4, 1]
    print("Max:", find_max(data))
    print("Min:", find_min(data))
    print("Average:", average(data))
    print("Unique:", remove_duplicates(data))
