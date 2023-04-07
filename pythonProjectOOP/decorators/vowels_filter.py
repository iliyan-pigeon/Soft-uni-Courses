from functools import wraps


def vowel_filter(function):
    vowels = ["a", "e", "i", "o", "u", "y"]
    found_vowels = []

    @wraps(function)
    def wrapper():
        for ch in function():
            if ch.lower() in vowels:
                found_vowels.append(ch)

        return found_vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
