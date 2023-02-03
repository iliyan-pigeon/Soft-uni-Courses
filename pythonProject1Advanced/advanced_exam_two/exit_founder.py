from collections import deque

tom_and_jerry = deque(input().split(", "))
matrix_maze = [input().split() for row in range(6)]
banned_players = []

while True:
    row, col = map(int, input().strip("()").split(", "))

    if tom_and_jerry[0] in banned_players:
        banned_players.remove(tom_and_jerry[0])
        tom_and_jerry.append(tom_and_jerry.popleft())
        continue
    if matrix_maze[row][col] == "E":
        print(f"{tom_and_jerry.popleft()} found the Exit and wins the game!" )
        break
    elif matrix_maze[row][col] == "T":
        print(f"{tom_and_jerry.popleft()} is out of the game! The winner is {tom_and_jerry.pop()}." )
        break
    elif matrix_maze[row][col] == "W":
        print(f"{tom_and_jerry[0]} hits a wall and needs to rest.")
        banned_players.append(tom_and_jerry[0])

    tom_and_jerry.append(tom_and_jerry.popleft())
