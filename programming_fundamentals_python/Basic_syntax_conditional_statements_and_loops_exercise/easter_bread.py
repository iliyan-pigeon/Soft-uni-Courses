budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_litre_milk = price_kg_flour + (price_kg_flour * 0.25)
total_loaves = 0
total_eggs = 0
iterations_counter = 0
can_buy = True
while can_buy:
    iterations_counter += 1
    current_price = price_kg_flour + price_pack_eggs + (price_litre_milk / 4)
    if current_price <= budget:
        budget -= current_price
        total_loaves += 1
        total_eggs += 3
    else:
        can_buy = False
        break
    if iterations_counter == 3:
        iterations_counter = 0
        total_eggs -= (total_loaves-2)
print(f"You made {total_loaves} loaves of Easter bread! Now you have {total_eggs} eggs and {budget:.2f}BGN left.")