def palindrome_decider(numbers_list: list):
    reversed_list = []
    for number in numbers_list:
        reversed_number = []
        for character in range(len(number)-1, -1, -1):
            reversed_number.append(number[character])
        reversed_list.append("".join(reversed_number))
    for number in range(0, len(numbers_list)):
        if numbers_list[number] == reversed_list[number]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")
palindrome_decider(numbers)



