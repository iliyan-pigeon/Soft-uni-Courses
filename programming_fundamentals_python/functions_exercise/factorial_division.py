def factorial_divider(first, second):
    factorial_first = first
    factorial_second = second
    for number in range(1, first):
        factorial_first *= number
    for number in range(1, second):
        factorial_second *= number
    return f"{factorial_first / factorial_second:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_divider(first_number, second_number))
