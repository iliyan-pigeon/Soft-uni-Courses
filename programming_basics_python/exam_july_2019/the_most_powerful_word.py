import math

word = input()
strongest_word = ""
strongest_word_power = 0
while word != "End of words":
    word_length = 0
    word_power = 0
    should_multiply = False
    for i, d in enumerate(word):
        word_power += ord(d)
        word_length += 1
        if i == 0:
            d = d.lower()
            if d == "a" or d == "e" or d == "i" or d == "o" or \
                    d == "u" or d == "y":
                should_multiply = True
    if should_multiply:
        word_power *= word_length
    elif not should_multiply:
        word_power = math.floor(word_power / word_length)
    if word_power > strongest_word_power:
        strongest_word_power = word_power
        strongest_word = word
    word = input()
print(f"The most powerful word is {strongest_word} - {strongest_word_power}")
