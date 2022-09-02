fires_information = input().split("#")
water_amount = int(input())
total_effort = 0
total_fire = 0
print("Cells:")
for fire in fires_information:
    the_fire = fire.split(" = ")
    fire_type = the_fire[0]
    fire_quality = int(the_fire[1])
    if fire_type == "High" and 81 <= fire_quality <= 125:
        if water_amount - fire_quality >= 0:
            water_amount -= fire_quality
            total_effort += fire_quality * 0.25
            total_fire += fire_quality
            print(f" - {fire_quality}")
    elif fire_type == "Medium" and 51 <= fire_quality <= 80:
        if water_amount - fire_quality >= 0:
            water_amount -= fire_quality
            total_effort += fire_quality * 0.25
            total_fire += fire_quality
            print(f" - {fire_quality}")
    elif fire_type == "Low" and 1 <= fire_quality <= 50:
        if water_amount - fire_quality >= 0:
            water_amount -= fire_quality
            total_effort += fire_quality * 0.25
            total_fire += fire_quality
            print(f" - {fire_quality}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")