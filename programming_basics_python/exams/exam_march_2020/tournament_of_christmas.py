tournament_days = int(input())
total_money = 0
days_won = 0
days_lost = 0
won_tournament = False
for day in range(tournament_days):
    sport_type = input()
    current_wins = 0
    current_losses = 0
    current_money = 0
    while sport_type != "Finish":
        outcome = input()
        if outcome == "win":
            current_wins += 1
            current_money += 20
        elif outcome == "lose":
            current_losses += 1
        sport_type = input()
    if current_wins > current_losses:
        days_won += 1
        current_money += (current_money * 0.1)
    elif current_wins < current_losses:
        days_lost += 1
    total_money += current_money
if days_won > days_lost:
    won_tournament = True
    total_money += (total_money * 0.2)
if won_tournament:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
elif not won_tournament:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")