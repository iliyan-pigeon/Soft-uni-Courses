letters_number = int(input())
for first_letter in range(97, 97+letters_number):
    for second_letter in range(97, 97+letters_number):
        for third_letter in range(97, 97+letters_number):
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")
