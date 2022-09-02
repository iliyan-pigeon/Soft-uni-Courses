wall_height = int(input())
wall_width = int(input())
percent_windows_walls = int(input())
current_litres_paint = input()
difference = 0
sq_m_painted = 0
job_done = False
sq_m_for_paint = wall_height * wall_width * 4 \
                 - ((wall_width * wall_height * 4) * percent_windows_walls / 100)
while current_litres_paint != "Tired!":
    current_sq_m = int(current_litres_paint)
    sq_m_painted += current_sq_m
    if sq_m_painted >= sq_m_for_paint:
        job_done = True
        break
    current_litres_paint = input()
difference = int(abs(sq_m_for_paint - sq_m_painted))
if job_done:
    if difference == 0:
        print("All walls are painted! Great job, Pesho!")
    elif difference != 0:
        print(f"All walls are painted and you have {difference} l paint left!")
elif not job_done:
    print(f"{difference} quadratic m left.")
