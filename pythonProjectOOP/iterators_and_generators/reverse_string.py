def reverse_text(text):
    while text:
        yield text[-1]
        text = text.replace(text[-1], "")


for char in reverse_text("step"):
    print(char, end='')