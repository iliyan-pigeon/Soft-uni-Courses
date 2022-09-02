nylon_price_sq_m = 1.50
paint_per_litre = 14.50
thinner_per_litre = 5.00
bags = 0.40
amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
hours_needed = int(input())
nylon_price = nylon_price_sq_m * amount_of_nylon + nylon_price_sq_m * 2
paint_price = paint_per_litre * (amount_of_paint + (amount_of_paint * 10 / 100))
thinner_price = thinner_per_litre * amount_of_thinner
price_consumables = nylon_price + paint_price + thinner_price + bags
salary_per_hour = price_consumables * 30 / 100
workers_total_salary = salary_per_hour * hours_needed
final_price = price_consumables + workers_total_salary
print(final_price)