beyond_twenty_kilo_price = float(input())
luggage_weight = float(input())
days_to_flight = int(input())
number_of_luggage = int(input())
under_ten_kilo_price = beyond_twenty_kilo_price * 0.2
between_ten_twenty_kilo_price = beyond_twenty_kilo_price * 0.5
more_than_thirty_day_tax_percent = 0.1
between_seven_thirty_day_tax_percent = 0.15
less_than_seven_days_tax_percent = 0.4
final_price_luggage = 0
if luggage_weight > 20:
    if days_to_flight > 30:
        final_price_luggage = (beyond_twenty_kilo_price + \
        (beyond_twenty_kilo_price * more_than_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight >= 7:
        final_price_luggage = (beyond_twenty_kilo_price + \
        (beyond_twenty_kilo_price * between_seven_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight < 7:
        final_price_luggage = (beyond_twenty_kilo_price + \
        (beyond_twenty_kilo_price * less_than_seven_days_tax_percent)) * number_of_luggage
elif luggage_weight >= 10:
    if days_to_flight > 30:
        final_price_luggage = (between_ten_twenty_kilo_price + \
        (between_ten_twenty_kilo_price * more_than_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight >= 7:
        final_price_luggage = (between_ten_twenty_kilo_price + \
        (between_ten_twenty_kilo_price * between_seven_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight < 7:
        final_price_luggage = (between_ten_twenty_kilo_price + \
        (between_ten_twenty_kilo_price * less_than_seven_days_tax_percent)) * number_of_luggage
elif luggage_weight < 10:
    if days_to_flight > 30:
        final_price_luggage = (under_ten_kilo_price + \
        (under_ten_kilo_price * more_than_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight >= 7:
        final_price_luggage = (under_ten_kilo_price + \
        (under_ten_kilo_price * between_seven_thirty_day_tax_percent)) * number_of_luggage
    elif days_to_flight < 7:
        final_price_luggage = (under_ten_kilo_price + \
        (under_ten_kilo_price * less_than_seven_days_tax_percent)) * number_of_luggage
print(f"The total price of bags is: {final_price_luggage:.2f} lv.")
