first_sequence = set(int(i) for i in input().split())
second_sequence = set(int(i) for i in input().split())
commands_amount = int(input())
for i in range(commands_amount):
    command = input()
    if "Add First" in command:
        command = command.split()
        for ch in command:
            if ch.isnumeric():
                first_sequence.add(int(ch))
    elif "Add Second" in command:
        command = command.split()
        for ch in command:
            if ch.isnumeric():
                second_sequence.add(int(ch))
    elif "Remove First" in command:
        command = command.split()
        for ch in command:
            if ch.isnumeric() and int(ch) in first_sequence:
                first_sequence.remove(int(ch))
    elif "Remove Second" in command:
        command = command.split()
        for ch in command:
            if ch.isnumeric() and int(ch) in second_sequence:
                second_sequence.remove(int(ch))
    elif command == "Check Subset":
        if first_sequence.issubset(second_sequence):
            print("True")
        elif second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")
ordered_first_sequence = ", ".join(str(i) for i in sorted(first_sequence))
ordered_second_sequence = ", ".join(str(i) for i in sorted(second_sequence))
print(ordered_first_sequence)
print(ordered_second_sequence)


