"""String helper functions for practice."""


def reverse_string(text):
    """Return text reversed."""
    return text[::-1]


def is_palindrome(text):
    """Return True if text reads same forwards and backwards (ignores case)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Return number of vowels in text."""
    return sum(1 for char in text.lower() if char in "aeiou")


def to_title_case(text):
    """Return text with each word capitalized."""
    return text.title()


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(is_palindrome("Race car"))
    print(count_vowels("education"))
    print(to_title_case("git practice session"))
