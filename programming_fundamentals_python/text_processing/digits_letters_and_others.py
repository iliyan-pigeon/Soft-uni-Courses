def find_digits(text):
    return "".join([i for i in text if i.isdigit()])


def find_letters(text):
    return "".join([i for i in text if i.isalpha()])


def find_symbols(text):
    return "".join([i for i in text if i.isdigit() == False and i.isalpha() == False])


the_text = input()
print(find_digits(the_text))
print(find_letters(the_text))
print(find_symbols(the_text))
