"""Temperature conversion functions for git practice."""


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


if __name__ == "__main__":
    print("100C =", celsius_to_fahrenheit(100), "F")
    print("32F =", fahrenheit_to_celsius(32), "C")
    print("0C =", celsius_to_kelvin(0), "K")
