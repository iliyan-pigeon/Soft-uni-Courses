number_of_moves = int(input())
invalid_numbers = 0
percent_invalid_numbers = 0
numbers_from_zero_to_nine = 0
percent_from_zero_to_nine = 0
numbers_from_ten_to_nineteen = 0
percent_from_ten_to_nineteen = 0
numbers_from_twenty_to_twenty_nine = 0
percent_from_twenty_to_twenty_nine = 0
numbers_from_thirty_to_thirty_nine = 0
percent_from_thirty_to_thirty_nine = 0
numbers_from_forty_to_fifty = 0
percent_from_forty_to_fifty = 0
total_score = 0
for move in range(number_of_moves):
    current_number = int(input())
    if 0 <= current_number < 10:
        numbers_from_zero_to_nine += 1
        total_score += current_number * 0.2
    elif 10 <= current_number < 20:
        numbers_from_ten_to_nineteen += 1
        total_score += current_number * 0.3
    elif 20 <= current_number < 30:
        numbers_from_twenty_to_twenty_nine += 1
        total_score += current_number * 0.4
    elif 30 <= current_number < 40:
        numbers_from_thirty_to_thirty_nine += 1
        total_score += 50
    elif 40 <= current_number <= 50:
        numbers_from_forty_to_fifty += 1
        total_score += 100
    elif current_number < 0 or current_number > 50:
        invalid_numbers += 1
        total_score = total_score / 2
percent_from_zero_to_nine = numbers_from_zero_to_nine / number_of_moves * 100
percent_from_ten_to_nineteen = numbers_from_ten_to_nineteen / number_of_moves * 100
percent_from_twenty_to_twenty_nine = numbers_from_twenty_to_twenty_nine / number_of_moves * 100
percent_from_thirty_to_thirty_nine = numbers_from_thirty_to_thirty_nine / number_of_moves * 100
percent_from_forty_to_fifty = numbers_from_forty_to_fifty / number_of_moves * 100
percent_invalid_numbers = invalid_numbers / number_of_moves * 100
print(f"{total_score:.2f}")
print(f"From 0 to 9: {percent_from_zero_to_nine:.2f}%")
print(f"From 10 to 19: {percent_from_ten_to_nineteen:.2f}%")
print(f"From 20 to 29: {percent_from_twenty_to_twenty_nine:.2f}%")
print(f"From 30 to 39: {percent_from_thirty_to_thirty_nine:.2f}%")
print(f"From 40 to 50: {percent_from_forty_to_fifty:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")