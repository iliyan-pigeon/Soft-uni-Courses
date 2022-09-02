heritage = float(input())
year_of_death = int(input())
difference = 0
total_expenses = 0
age_of_ivan = 18
for year in range(1800, year_of_death + 1):
    if year % 2 == 0:
        total_expenses += 12000
    else:
        total_expenses += (12000 + 50 * age_of_ivan)
    age_of_ivan += 1
difference = abs(heritage - total_expenses)
if heritage >= total_expenses:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
elif heritage < total_expenses:
    print(f"He will need {difference:.2f} dollars to survive.")