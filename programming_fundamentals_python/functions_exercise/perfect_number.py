def perfect_number(number: int):
    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == number:
        return "We have a perfect number!"
    return "It's not so perfect."


the_number = int(input())
print(perfect_number(the_number))
