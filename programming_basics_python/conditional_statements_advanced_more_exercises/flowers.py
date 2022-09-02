chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
is_it_weekend = input()
discount_one = 0
discount_two = 0
discount_three = 0
weekend_raise = 0.15
arrangement = 2
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
total_chrysanthemums = 0
total_roses = 0
total_tulips = 0
total_price = 0
final_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
    if is_it_weekend == "Y":
        chrysanthemum_price = chrysanthemum_price + (chrysanthemum_price * weekend_raise)
        rose_price = rose_price + (rose_price * weekend_raise)
        tulip_price = tulip_price + (tulip_price * weekend_raise)
    elif is_it_weekend == "N":
        pass
    total_chrysanthemums = chrysanthemum_price * chrysanthemums_number
    total_roses = rose_price * roses_number
    total_tulips = tulip_price * tulips_number
    total_price = total_chrysanthemums + total_roses + total_tulips
    if season == "Spring" and tulips_number > 7:
        discount_one = total_price * 0.05
    final_price = total_price - discount_one
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15
    if is_it_weekend == "Y":
        chrysanthemum_price = chrysanthemum_price + (chrysanthemum_price * weekend_raise)
        rose_price = rose_price + (rose_price * weekend_raise)
        tulip_price = tulip_price + (tulip_price * weekend_raise)
    elif is_it_weekend == "N":
        pass
    total_chrysanthemums = chrysanthemum_price * chrysanthemums_number
    total_roses = rose_price * roses_number
    total_tulips = tulip_price * tulips_number
    total_price = total_chrysanthemums + total_roses + total_tulips
    if season == "Winter" and roses_number >= 10:
        discount_two = total_price * 0.1
    final_price = total_price - discount_two
if chrysanthemums_number + roses_number + tulips_number > 20:
    discount_three = final_price * 0.2
price_to_pay = (final_price + arrangement) - discount_three
print(f"{price_to_pay:.2f}")




