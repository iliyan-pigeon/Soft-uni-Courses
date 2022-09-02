guests_number = int(input())
envelope_price = float(input())
budget = float(input())
discount = 0
total_envelopes_price = 0
cake_price = budget * 0.1
if guests_number >= 10 and guests_number <= 15:
    discount = 0.15
    envelope_price -= (envelope_price * discount)
elif guests_number > 15 and guests_number <= 20:
    discount = 0.2
    envelope_price -= (envelope_price * discount)
elif guests_number > 20:
    discount = 0.25
    envelope_price -= (envelope_price * discount)
total_envelopes_price = guests_number * envelope_price
total_price = total_envelopes_price + cake_price
difference = abs(total_price - budget)
if total_price <= budget:
    print(f"It is party time! {difference:.2f} leva left.")
elif total_price > budget:
    print(f"No party! {difference:.2f} leva needed.")
