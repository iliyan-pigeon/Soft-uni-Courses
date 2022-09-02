import sys

films_number = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_rated_film = ""
lowest_rated_film = ""
combined_ratings = 0
average_rating = 0
for film in range(films_number):
    film_name = input()
    film_rating = float(input())
    combined_ratings += film_rating
    if film_rating > highest_rating:
        highest_rating = film_rating
        highest_rated_film = film_name
    elif film_rating < lowest_rating:
        lowest_rating = film_rating
        lowest_rated_film = film_name
average_rating = combined_ratings / films_number
print(f"{highest_rated_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rated_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
