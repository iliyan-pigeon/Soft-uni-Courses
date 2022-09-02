number_of_cargo = int(input())
average_price_per_ton = 0
price_per_ton_minibus = 200
price_per_ton_truck = 175
price_per_ton_train = 120
price_for_minibus = 0
price_for_truck = 0
price_for_train = 0
total_price = 0
percent_minibus = 0
percent_truck = 0
percent_train = 0
weight_with_minibus = 0
weight_with_truck = 0
weight_with_train = 0
total_weight_cargo = 0
for cargo in range(number_of_cargo):
    current_cargo_weight = int(input())
    if current_cargo_weight <= 3:
        weight_with_minibus += current_cargo_weight
    elif current_cargo_weight <= 11:
        weight_with_truck += current_cargo_weight
    elif current_cargo_weight > 11:
        weight_with_train += current_cargo_weight
price_for_minibus = weight_with_minibus * price_per_ton_minibus
price_for_truck = weight_with_truck * price_per_ton_truck
price_for_train = weight_with_train * price_per_ton_train
total_price = price_for_minibus + price_for_truck + price_for_train
total_weight_cargo = weight_with_minibus + weight_with_truck + weight_with_train
average_price_per_ton = total_price / total_weight_cargo
percent_minibus = weight_with_minibus / total_weight_cargo * 100
percent_truck = weight_with_truck / total_weight_cargo * 100
percent_train = weight_with_train / total_weight_cargo * 100
print(f"{average_price_per_ton:.2f}")
print(f"{percent_minibus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")