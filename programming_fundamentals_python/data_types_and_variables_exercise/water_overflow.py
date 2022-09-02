number_of_pours = int(input())
pool_capacity = 255
total_water = 0
for pour in range(number_of_pours):
    current_pour = int(input())
    if current_pour + total_water > pool_capacity:
        print("Insufficient capacity!")
    elif current_pour + total_water <= pool_capacity:
        total_water += current_pour
print(total_water)