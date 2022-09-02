import math

number_magnolias = int(input())
number_hyacinths = int(input())
number_roses = int(input())
number_cacti = int(input())
gift_price = float(input())
one_magnolia_price = 3.25
one_hyacinth_price = 4
one_rose_price = 3.5
one_cactus_price = 8
magnolias_price = number_magnolias * one_magnolia_price
hyacinths_price = number_hyacinths * one_hyacinth_price
roses_price = number_roses * one_rose_price
cacti_price = number_cacti * one_cactus_price
total_price = magnolias_price + hyacinths_price + roses_price\
    + cacti_price
tax_amount = total_price * 0.05
final_price = total_price - tax_amount
difference = abs(final_price - gift_price)
if final_price >= gift_price:
    print(f"She is left with {math.floor(difference)} leva." )
elif final_price < gift_price:
    print(f"She will have to borrow {math.ceil(difference)} leva.")