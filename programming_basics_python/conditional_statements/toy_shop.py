puzzle_price = 2.60
talking_doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00
excursion_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
number_of_toys = number_puzzles + number_dolls \
    + number_bears + number_minions + number_trucks
toys_price_combined = puzzle_price * number_puzzles \
    + talking_doll_price * number_dolls + teddy_bear_price * number_bears \
    + minion_price * number_minions + truck_price * number_trucks
if number_of_toys >= 50:
    toys_price_combined = toys_price_combined - toys_price_combined * 0.25
price_after_rent = toys_price_combined - toys_price_combined * 0.1
if excursion_price <= price_after_rent:
    remaining = price_after_rent - excursion_price
    print(f'Yes! {remaining:.2f} lv left.')
elif excursion_price > price_after_rent:
    needed = excursion_price - price_after_rent
    print(f'Not enough money! {needed:.2f} lv needed.')



