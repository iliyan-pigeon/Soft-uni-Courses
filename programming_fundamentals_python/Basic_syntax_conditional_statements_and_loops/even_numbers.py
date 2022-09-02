numbers = int(input())
all_are_even = True
for number in range(numbers):
    current_number = int(input())
    if current_number % 2 != 0:
        all_are_even = False
        print(f"{current_number} is odd!")
        break
if all_are_even:
    print("All numbers are even.")