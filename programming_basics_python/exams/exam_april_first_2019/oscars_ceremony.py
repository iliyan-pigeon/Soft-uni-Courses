hall_rent = int(input())
statuettes = hall_rent * 0.7
catering = statuettes * 0.85
sound_system = catering / 2
total_price = hall_rent + statuettes + \
    catering + sound_system
print(f"{total_price:.2f}")