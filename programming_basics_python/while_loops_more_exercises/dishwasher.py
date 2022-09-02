number_detergent_bottles = int(input())
ml_per_bottle = 750
total_detergent_ml = ml_per_bottle * number_detergent_bottles
detergent_for_one_plate = 5
detergent_for_one_pot = 15
clean_plates = 0
clean_pots = 0
needed_detergent = 0
difference = 0
loading = 0
current_dishes = input()
while current_dishes != "End" and needed_detergent <= total_detergent_ml:
    number_dishes = int(current_dishes)
    if loading == 2:
        clean_pots += number_dishes
        needed_detergent += detergent_for_one_pot * number_dishes
        loading = 0
    else:
        clean_plates += number_dishes
        needed_detergent += detergent_for_one_plate * number_dishes
        loading += 1
    if needed_detergent <= total_detergent_ml:
        current_dishes = input()
difference = abs(needed_detergent - total_detergent_ml)
if needed_detergent <= total_detergent_ml:
    print("Detergent was enough!")
    print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
elif needed_detergent > total_detergent_ml:
    print(f"Not enough detergent, {difference} ml. more necessary!")