t_shirt_price = float(input())
needed_price = float(input())
shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
football_shoes_price = (t_shirt_price + shorts_price) * 2
total_price = t_shirt_price + shorts_price + socks_price + football_shoes_price
discount = total_price * 0.15
final_price = total_price - discount
if final_price >= needed_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_price:.2f} lv.")
else:
    difference = abs(final_price - needed_price)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")