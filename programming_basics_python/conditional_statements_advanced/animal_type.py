animal_type = input()
mammal = animal_type == "dog"
reptile = animal_type == "crocodile" or animal_type == "snake" \
    or animal_type == "tortoise"
if mammal:
    print("mammal")
elif reptile:
    print("reptile")
else:
    print("unknown")