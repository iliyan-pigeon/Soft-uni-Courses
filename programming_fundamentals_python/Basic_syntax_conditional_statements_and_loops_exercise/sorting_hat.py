name = input()
sorted_successfully = True
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        sorted_successfully = False
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if sorted_successfully:
    print("Welcome to Hogwarts.")