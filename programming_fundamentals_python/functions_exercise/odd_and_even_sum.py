def even_odd_sums(number_as_string):
    even_list = []
    odd_list = []
    for character in number_as_string:
        if int(character) % 2 == 0:
            even_list.append(int(character))
        elif int(character) % 2 != 0:
            odd_list.append(int(character))
    return f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}"


number = input()
print(even_odd_sums(number))

