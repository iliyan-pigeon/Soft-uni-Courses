airline_name = input()
number_tickets_adults = int(input())
number_tickets_kids = int(input())
net_price_ticket_adult = float(input())
tax_service = float(input())
net_price_ticket_kid = net_price_ticket_adult * 0.3
total_price_adult_tickets = (net_price_ticket_adult + tax_service) * number_tickets_adults
total_price_kid_tickets = (net_price_ticket_kid + tax_service) * number_tickets_kids
total_price_tickets = total_price_kid_tickets + total_price_adult_tickets
company_profit = total_price_tickets * 0.2
print(f"The profit of your agency from {airline_name} tickets is {company_profit:.2f} lv.")
