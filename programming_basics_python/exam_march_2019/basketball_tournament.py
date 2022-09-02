tournament_name = input()
difference = 0
number_matches = 0
matches_won = 0
matches_loss = 0
percent_wins = 0
percent_losses = 0
while tournament_name != "End of tournaments":
    number_of_matches = int(input())
    for match in range(1, number_of_matches + 1):
        points_scored = int(input())
        points_received = int(input())
        number_matches += 1
        difference = abs(points_scored - points_received)
        if points_scored > points_received:
            matches_won += 1
            print(f"Game {match} of tournament {tournament_name}: win with {difference} points.")
        elif points_scored < points_received:
            matches_loss += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {difference} points.")
    tournament_name = input()
percent_wins = matches_won / number_matches * 100
percent_losses = matches_loss / number_matches * 100
print(f"{percent_wins:.2f}% matches win")
print(f"{percent_losses:.2f}% matches lost")