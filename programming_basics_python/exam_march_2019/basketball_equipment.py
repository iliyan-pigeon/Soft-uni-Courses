annual_fee = int(input())
sneakers_price = annual_fee * 0.6
outfit_price = sneakers_price * 0.8
ball_price = outfit_price / 4
accessories = ball_price / 5
total_price = annual_fee + sneakers_price + outfit_price\
    + ball_price + accessories
print(f"{total_price:.2f}")