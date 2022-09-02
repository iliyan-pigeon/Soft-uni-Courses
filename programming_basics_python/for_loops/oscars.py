actor_name = input()
points_from_academy = float(input())
number_of_evaluators = int(input())
total_points = points_from_academy
total_evaluator_points = 0
difference = 0
is_nominated = False
for evaluator in range(number_of_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())
    total_evaluator_points = len(evaluator_name) * evaluator_points / 2
    total_points += total_evaluator_points
    if total_points > 1250.5:
        is_nominated = True
        break
if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
if not is_nominated:
    difference = abs(total_points - 1250.5)
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")

