type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
discount_volume = 0
increase_volume = 0
total_sum = 0
price = 0
if type_of_flowers == "Roses":
    price = 5
    if number_of_flowers > 80:
        discount_volume = number_of_flowers * price * 0.1
    total_sum = number_of_flowers * price - discount_volume
elif type_of_flowers == "Dahlias":
    price = 3.8
    if number_of_flowers > 90:
        discount_volume = number_of_flowers * price * 0.15
    total_sum = number_of_flowers * price - discount_volume
elif type_of_flowers == "Tulips":
    price = 2.8
    if number_of_flowers > 80:
        discount_volume = number_of_flowers * price * 0.15
    total_sum = number_of_flowers * price - discount_volume
elif type_of_flowers == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        increase_volume = number_of_flowers * price * 0.15
    total_sum = number_of_flowers * price + increase_volume
elif type_of_flowers == "Gladiolus":
    price = 2.5
    if number_of_flowers < 80:
        increase_volume = number_of_flowers * price * 0.2
    total_sum = number_of_flowers * price + increase_volume
if total_sum <= budget:
    difference = abs(budget - total_sum)
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
elif total_sum > budget:
    difference = abs(total_sum - budget)
    print(f"Not enough money, you need {difference:.2f} leva more.")

