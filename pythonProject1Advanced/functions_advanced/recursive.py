def recursive_power(number, power):
    result = number
    for i in range(power-1):
        result *= number
    return result


print(recursive_power(2, 10))