command = input()
coffees_number = 0
while command != "END":
    more_coffee = False
    if command == "coding" or command == "CODING":
        more_coffee = True
    elif command == "dog" or command == "DOG":
        more_coffee = True
    elif command == "cat" or command == "CAT":
        more_coffee = True
    elif command == "movie" or command == "MOVIE":
        more_coffee = True
    else:
        pass
    if more_coffee:
        if command.islower():
            coffees_number += 1
        elif command.isupper():
            coffees_number += 2
    command = input()
if coffees_number > 5:
    print("You need extra sleep")
else:
    print(coffees_number)