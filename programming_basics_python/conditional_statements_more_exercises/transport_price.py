kilometres_to_travel = int(input())
day_or_night = input()
total_price = 0
if kilometres_to_travel < 20:
    initial_fee_taxi = 0.7
    tariff_per_km_day = 0.79
    tariff_per_km_night = 0.9
    if day_or_night == "day":
        total_price = initial_fee_taxi + tariff_per_km_day * kilometres_to_travel
    elif day_or_night == "night":
        total_price = initial_fee_taxi + tariff_per_km_night * kilometres_to_travel
elif 20 <= kilometres_to_travel < 100:
    tariff_per_km = 0.09
    total_price = tariff_per_km * kilometres_to_travel
elif kilometres_to_travel >= 100:
    tariff_per_km = 0.06
    total_price = tariff_per_km * kilometres_to_travel
print(f"{total_price:.2f}")
