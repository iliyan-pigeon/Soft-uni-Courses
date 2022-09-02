club_name = input()
games_number = int(input())
total_points = 0
percent_wins = 0
games_won = 0
games_drawn = 0
games_lost = 0
for game in range(games_number):
    game_outcome = input()
    if game_outcome == "W":
        games_won += 1
        total_points += 3
    elif game_outcome == "D":
        games_drawn += 1
        total_points += 1
    elif game_outcome == "L":
        games_lost += 1
if games_number == 0:
    print(f"{club_name} hasn't played any games during this season.")
elif games_number > 0:
    percent_wins = games_won / games_number * 100
    print(f"{club_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {games_won}")
    print(f"## D: {games_drawn}")
    print(f"## L: {games_lost}")
    print(f"Win rate: {percent_wins:.2f}%")