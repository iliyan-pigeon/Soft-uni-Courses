characters = input()


def chars_amount(word):
    chars_dict = {}
    result = ""
    for char in word:
        if char == " ":
            continue
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1
    for key in chars_dict:
        result += f"{key} -> {chars_dict[key]}\n"
    return result


print(chars_amount(characters))
