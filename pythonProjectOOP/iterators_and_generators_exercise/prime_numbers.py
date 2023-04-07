def get_primes(numbers_list):
    for number in numbers_list:
        if number <= 1:
            continue

        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))