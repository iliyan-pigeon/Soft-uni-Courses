import os


def create(name):
    with open(f"./{name}", "w") as text:
        pass


def add(name, the_content):
    with open(f"./{name}", "a") as text:
        text.write(f"{the_content}\n")


def replace(name, previous, current):
    try:
        with open(f"./{name}", "r") as text:
            text = text.readlines()
        with open(f"./{name}", "w") as file_text:
            for i in range(len(text)):
                if previous in text[i]:
                    text[i] = text[i].replace(previous, current)
            file_text.write("".join(text))
    except FileNotFoundError:
        print("An error occurred")


def delete(name):
    try:
        os.remove(f"./{name}")
    except FileNotFoundError:
        print("An error occurred")


command = input()
while command != "End":
    command = command.split("-")
    the_command = command[0]
    if the_command == "Create":
        file_name = command[1]
        create(file_name)
    elif the_command == "Add":
        file_name = command[1]
        content = command[2]
        add(file_name, content)
    elif the_command == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        replace(file_name, old_string, new_string)
    elif the_command == "Delete":
        file_name = command[1]
        delete(file_name)
    command = input()
