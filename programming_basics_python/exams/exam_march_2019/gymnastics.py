country = input()
discipline = input()
difficulty_points = 0
performance_points = 0
total_points = 0
max_points = 20
percent = 0
if country == "Russia":
    if discipline == "ribbon":
        difficulty_points = 9.100
        performance_points = 9.400
    elif discipline == "hoop":
        difficulty_points = 9.300
        performance_points = 9.800
    elif discipline == "rope":
        difficulty_points = 9.600
        performance_points = 9.00
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty_points = 9.600
        performance_points = 9.400
    elif discipline == "hoop":
        difficulty_points = 9.550
        performance_points = 9.750
    elif discipline == "rope":
        difficulty_points = 9.5
        performance_points = 9.4
elif country == "Italy":
    if discipline == "ribbon":
        difficulty_points = 9.200
        performance_points = 9.500
    elif discipline == "hoop":
        difficulty_points = 9.450
        performance_points = 9.350
    elif discipline == "rope":
        difficulty_points = 9.700
        performance_points = 9.150
total_points = difficulty_points + performance_points
percent = 100 - (total_points / max_points * 100)
print(f"The team of {country} get {total_points:.3f} on {discipline}.")
print(f"{percent:.2f}%")
