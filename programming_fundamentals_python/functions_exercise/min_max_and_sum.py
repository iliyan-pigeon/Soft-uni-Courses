def numbers_stats(numbers: list):
    return f"The minimum number is {min(numbers)}\n" \
           f"The maximum number is {max(numbers)}\n" \
           f"The sum number is: {sum(numbers)}"


the_numbers = [int(number) for number in input().split()]
print(numbers_stats(the_numbers))


