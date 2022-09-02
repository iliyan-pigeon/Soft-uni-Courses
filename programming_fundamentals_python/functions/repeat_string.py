def repeat_string(letters, number):
    result = letters * number
    return result


letters = input()
number = int(input())
print(repeat_string(letters, number))
