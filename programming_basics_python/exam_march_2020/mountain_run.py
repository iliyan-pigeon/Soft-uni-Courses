import math

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_meter = float(input())
incline_slowdown = (math.floor(distance_in_meters / 50) * 30)
total_time = (distance_in_meters * seconds_for_meter) + incline_slowdown
if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
elif total_time >= record_in_seconds:
    difference = abs(total_time - record_in_seconds)
    print(f"No! He was {difference:.2f} seconds slower.")