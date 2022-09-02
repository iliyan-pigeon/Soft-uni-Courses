letters_number = int(input())
final_string = ""
for first_letter in range(97, 97+letters_number):
    for second_letter in range(97, 97+letters_number):
        for third_letter in range(97, 97+letters_number):
            final_string = chr(first_letter) + chr(second_letter) + chr(third_letter)
            print(final_string)
