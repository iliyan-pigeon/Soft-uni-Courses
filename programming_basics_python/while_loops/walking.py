steps_goal = 10000
goal_reached = True
daily_steps = 0
difference = 0
while daily_steps < steps_goal:
    current_steps = input()
    if current_steps == "Going home":
        steps_to_home = int(input())
        daily_steps += steps_to_home
        if daily_steps < steps_goal:
            goal_reached = False
        break
    else:
        steps_per_exit = int(current_steps)
        daily_steps += steps_per_exit
difference = abs (daily_steps - steps_goal)
if goal_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
elif not goal_reached:
    print(f"{difference} more steps to reach goal.")
