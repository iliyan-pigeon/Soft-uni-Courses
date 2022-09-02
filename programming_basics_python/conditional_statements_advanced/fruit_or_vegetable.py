#name = input()
#fruit = name == "banana" or name == "apple" \
#or name == "kiwi" or name == "cherry" or name == "lemon" \
#or name == "grapes"
#vegetable = name == "tomato" or name == "cucumber" \
#or name == "pepper" or name == "carrot"
#if fruit:
#    print("fruit")
#elif vegetable:
#    print("vegetable")
#else:
#    print("unknown")
name = input()
if name == "banana" or name == "apple" \
or name == "kiwi" or name == "cherry" or name == "lemon" \
or name == "grapes":
    print("fruit")
elif name ==  "tomato" or name == "cucumber" \
or name == "pepper" or name == "carrot":
    print("vegetable")
else:
    print("unknown")
