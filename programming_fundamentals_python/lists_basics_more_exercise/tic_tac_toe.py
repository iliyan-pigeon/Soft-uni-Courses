first_line = input().split()
second_line = input().split()
third_line = input().split()
first_player_winner = (first_line[0] == second_line[0] == third_line[0] and first_line[0] == '1' or
                       first_line[1] == second_line[1] == third_line[1] and first_line[1] == '1' or
                       first_line[2] == second_line[2] == third_line[2] and first_line[2] == '1' or
                       first_line[0] == first_line[1] == first_line[2] and first_line[0] == '1' or
                       second_line[0] == second_line[1] == second_line[2] and second_line[0] == '1' or
                       third_line[0] == third_line[1] == third_line[2] and third_line[0] == '1' or
                       first_line[0] == second_line[1] == third_line[2] and first_line[0] == '1' or
                       first_line[2] == second_line[1] == third_line[0] and first_line[2] == '1')


second_player_winner = (first_line[0] == second_line[0] == third_line[0] and first_line[0] == '2' or
                        first_line[1] == second_line[1] == third_line[1] and first_line[1] == '2' or
                        first_line[2] == second_line[2] == third_line[2] and first_line[2] == '2' or
                        first_line[0] == first_line[1] == first_line[2] and first_line[0] == '2' or
                        second_line[0] == second_line[1] == second_line[2] and second_line[0] == '2' or
                        third_line[0] == third_line[1] == third_line[2] and third_line[0] == '2' or
                        first_line[0] == second_line[1] == third_line[2] and first_line[0] == '2' or
                        first_line[2] == second_line[1] == third_line[0] and first_line[2] == '2')
if first_player_winner:
    print("First player won")
elif second_player_winner:
    print("Second player won")
else:
    print("Draw!")
