opened_tabs = int(input())
salary = int(input())
facebook_fine = 150
instagram_fine = 100
reddit_fine = 50
total_amount_penalty = 0
difference = 0
for tabs in range(opened_tabs):
    site_name = input()
    if site_name == "Facebook":
        total_amount_penalty += facebook_fine
    elif site_name == "Instagram":
        total_amount_penalty += instagram_fine
    elif site_name == "Reddit":
        total_amount_penalty += reddit_fine
difference = abs(total_amount_penalty - salary)
if salary > total_amount_penalty:
    print(difference)
elif salary <= total_amount_penalty:
    print("You have lost your salary.")

