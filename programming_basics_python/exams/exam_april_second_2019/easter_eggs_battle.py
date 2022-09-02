amount_eggs_first = int(input())
amount_eggs_second = int(input())
winner = input()
first_player_lost = 0
second_player_lost = 0
difference = 0
difference_two = 0
should_print = True
while winner != "End of battle":
    if winner == "one":
        second_player_lost += 1
    elif winner == "two":
        first_player_lost += 1
    if amount_eggs_first == first_player_lost:
        should_print = False
        difference = abs(amount_eggs_second - second_player_lost)
        print(f"Player one is out of eggs. Player two has {difference} eggs left.")
        break
    elif amount_eggs_second == second_player_lost:
        should_print = False
        difference = abs(amount_eggs_first - first_player_lost)
        print(f"Player two is out of eggs. Player one has {difference} eggs left.")
        break
    winner = input()
if should_print:
    difference = abs(amount_eggs_first - first_player_lost)
    difference_two = abs(amount_eggs_second - second_player_lost)
    print(f"Player one has {difference} eggs left.")
    print(f"Player two has {difference_two} eggs left.")