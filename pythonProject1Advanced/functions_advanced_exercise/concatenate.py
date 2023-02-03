def concatenate(*args, **kwargs):
    sentence = "".join(args)
    for key, value in kwargs.items():
        if key in sentence:
            sentence = sentence.replace(key, value)
    return sentence


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
                  UNI="Uni", Grate="Great"))
