messages_number = int(input())
for message in range(messages_number):
    current_message = int(input())
    if current_message == 88:
        print("Hello")
    elif current_message == 86:
        print("How are you?")
    elif current_message < 88:
        print("GREAT!")
    elif current_message > 88:
        print("Bye.")