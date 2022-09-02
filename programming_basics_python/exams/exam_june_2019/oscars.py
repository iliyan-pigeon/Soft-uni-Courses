actor_name = input()
academy_points = float(input())
evaluators_number = int(input())
total_points = academy_points
difference = 0
points_for_nomination = 1250.5
is_nominated = False
for evaluator in range(evaluators_number):
    name_length = 0
    evaluator_name = input()
    points_evaluator = float(input())
    for i in enumerate(evaluator_name):
        name_length += 1
    current_points = (name_length * points_evaluator) / 2
    total_points += current_points
    if total_points > points_for_nomination:
        is_nominated = True
        break
if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
elif not is_nominated:
    difference = abs(total_points - points_for_nomination)
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
