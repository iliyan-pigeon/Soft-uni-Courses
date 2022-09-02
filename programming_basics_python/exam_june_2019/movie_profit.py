movie_name = input()
days_number = int(input())
tickets_per_day = int(input())
ticket_price = float(input())
cinema_percent = int(input())
single_day_profit = ticket_price * tickets_per_day
brut_profit = days_number * single_day_profit
net_profit = brut_profit - (brut_profit * cinema_percent / 100)
print(f"The profit from the movie {movie_name} is {net_profit:.2f} lv.")