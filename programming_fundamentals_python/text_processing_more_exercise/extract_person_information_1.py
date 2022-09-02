sentences_amount = int(input())
storing_name = False
storing_age = False
for sentence in range(sentences_amount):
    current_sentence = input()
    name = ""
    age = ""
    for ch in current_sentence:
        if ch == "@":
            storing_name = True
        elif ch == "|":
            storing_name = False
        elif ch == "#":
            storing_age = True
        elif ch == "*":
            storing_age = False
        if storing_name:
            if not ch == "@":
                name += ch
        elif storing_age:
            if not ch == "#":
                age += ch
    print(f"{name} is {age} years old.")

