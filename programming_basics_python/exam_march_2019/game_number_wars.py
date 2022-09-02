name_first_player = input()
name_second_player = input()
points_first_player = 0
points_second_player = 0
difference = 0
should_print = True
first_player_card = input()
while first_player_card != "End of game":
    second_player_card = int(input())
    if int(first_player_card) > second_player_card:
        difference = abs(int(first_player_card) - second_player_card)
        points_first_player += difference
    elif int(first_player_card) < second_player_card:
        difference = abs(int(first_player_card) - second_player_card)
        points_second_player += difference
    elif int(first_player_card) == second_player_card:
        should_print = False
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print("Number wars!")
            print(f"{name_first_player} is winner with {points_first_player} points")
        elif first_player_card < second_player_card:
            print("Number wars!")
            print(f"{name_second_player} is winner with {points_second_player} points")
        break
    first_player_card = input()
if should_print:
    print(f"{name_first_player} has {points_first_player} points")
    print(f"{name_second_player} has {points_second_player} points")

