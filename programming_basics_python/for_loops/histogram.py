number_of_numbers = int(input())
numbers_to_two_hundred = 0
numbers_to_four_hundred = 0
numbers_to_six_hundred = 0
numbers_to_eight_hundred = 0
numbers_to_one_thousand = 0
percent_to_two_hundred  = 0
percent_to_four_hundred = 0
percent_to_six_hundred = 0
percent_to_eight_hundred = 0
percent_to_one_thousand = 0
for i in range(number_of_numbers):
    number = int(input())
    if number < 200:
        numbers_to_two_hundred += 1
    elif number < 400:
        numbers_to_four_hundred += 1
    elif number < 600:
        numbers_to_six_hundred +=1
    elif number < 800:
        numbers_to_eight_hundred += 1
    elif number <= 1000:
        numbers_to_one_thousand += 1
percent_to_two_hundred = numbers_to_two_hundred / number_of_numbers * 100
percent_to_four_hundred = numbers_to_four_hundred / number_of_numbers * 100
percent_to_six_hundred = numbers_to_six_hundred / number_of_numbers * 100
percent_to_eight_hundred = numbers_to_eight_hundred / number_of_numbers * 100
percent_to_one_thousand = numbers_to_one_thousand / number_of_numbers * 100
print(f"{percent_to_two_hundred:.2f}%")
print(f"{percent_to_four_hundred:.2f}%")
print(f"{percent_to_six_hundred:.2f}%")
print(f"{percent_to_eight_hundred:.2f}%")
print(f"{percent_to_one_thousand:.2f}%")