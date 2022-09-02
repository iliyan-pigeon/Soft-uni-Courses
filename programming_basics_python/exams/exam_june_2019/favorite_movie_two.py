film_name = input()
films_number = 0
highest_rating = 0
highest_rating_name = ""
reached_limit = False
while film_name != "STOP":
    films_number += 1
    film_name_length = 0
    current_film_rating = 0
    for s in film_name:
        film_name_length += 1
    for s in film_name:
        amount = ord(s)
        if s.isupper():
            current_film_rating += amount - film_name_length
        elif s.islower():
            current_film_rating += amount - (film_name_length * 2)
        else:
            current_film_rating += amount
    if current_film_rating > highest_rating:
        highest_rating = current_film_rating
        highest_rating_name = film_name
    if films_number >= 7:
        reached_limit = True
        break
    film_name = input()
if reached_limit:
    print("The limit is reached.")
print(f"The best movie for you is {highest_rating_name} with {highest_rating} ASCII sum.")