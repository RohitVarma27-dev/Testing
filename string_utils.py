"""String helper functions for git practice."""


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


if __name__ == "__main__":
    print(reverse("hello"))
    print(is_palindrome("race car"))
    print(count_vowels("education"))
    print(capitalize_words("hello world"))
