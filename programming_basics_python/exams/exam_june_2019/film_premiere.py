film_name = input()
film_package = input()
tickets_number = int(input())
ticket_price = 0
total_price = 0
final_price = 0
discount = 0
if film_name == "John Wick":
    if film_package == "Drink":
        ticket_price = 12
    elif film_package == "Popcorn":
        ticket_price = 15
    elif film_package == "Menu":
        ticket_price = 19
elif film_name == "Star Wars":
    if film_package == "Drink":
        ticket_price = 18
    elif film_package == "Popcorn":
        ticket_price = 25
    elif film_package == "Menu":
        ticket_price = 30
elif film_name == "Jumanji":
    if film_package == "Drink":
        ticket_price = 9
    elif film_package == "Popcorn":
        ticket_price = 11
    elif film_package == "Menu":
        ticket_price = 14
if film_name == "Star Wars" and tickets_number >= 4:
    total_price = ticket_price * tickets_number
    discount = total_price * 0.3
    final_price = total_price - discount
elif film_name == "Jumanji" and tickets_number == 2:
    total_price = ticket_price * tickets_number
    discount = total_price * 0.15
    final_price = total_price - discount
else:
    final_price = ticket_price * tickets_number
print(f"Your bill is {final_price:.2f} leva.")