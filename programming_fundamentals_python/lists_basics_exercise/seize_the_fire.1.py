fires_information = [str(fire) for fire in input().split('#')]
water_amount = int(input())
total_effort = 0
total_fire = 0
print("Cells:")
for fire in fires_information:
    fire = fire.split(" = ")
    fire_type = fire[0]
    fire_amount = int(fire[1])
    shut_it_down = False
    if fire_amount <= water_amount:
        if fire_type == "High" and 81 <= fire_amount <= 125:
            shut_it_down = True
        elif fire_type == "Medium" and 51 <= fire_amount <= 80:
            shut_it_down = True
        elif fire_type == "Low" and 1 <= fire_amount <= 50:
            shut_it_down = True
    if shut_it_down:
        water_amount -= fire_amount
        total_fire += fire_amount
        current_effort = fire_amount * 0.25
        total_effort += current_effort
        print(f" - {fire_amount}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")