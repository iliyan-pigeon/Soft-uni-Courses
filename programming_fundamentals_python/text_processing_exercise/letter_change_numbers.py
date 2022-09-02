def position(alphabet):
    return "{}".format(ord(alphabet) - 96)


texts = input().split()
result = 0
lower = True
for i in texts:
    text = i.strip()
    current_result = 0
    letter_in_number = 0
    number = ''
    second_letter = False
    for ch in range(len(text)):
        if text[ch].isalpha():
            if not second_letter:
                letter_in_number += int(position(text[ch].lower()))
                if text[ch].isupper():
                    lower = False
            elif second_letter:
                letter_in_number += int(position(text[ch].lower()))
                if text[ch].isupper():
                    lower = False
                if lower:
                    current_result += letter_in_number
                elif not lower:
                    current_result -= letter_in_number
                result += current_result
        else:
            number += text[ch]
            if text[ch+1].isalpha():
                if lower:
                    current_result = int(number) * letter_in_number
                elif not lower:
                    current_result = int(number) / letter_in_number
                letter_in_number = 0
                second_letter = True
                lower = True
print(f"{result:.2f}")

