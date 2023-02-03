while True:
    try:
        text = input("Please enter a text:")
        amount = int(input("Please enter number:"))
        result = text * amount
        print(result)
        break
    except ValueError:
        print("Oop! That was no valid number. Try again...")
