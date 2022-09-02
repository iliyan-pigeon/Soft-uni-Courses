sentence = input()
while sentence != "End":
    doubled_sentence = ""
    for i, d in enumerate(sentence):
        doubled_sentence += d * 2
    if sentence != "SoftUni":
        print(doubled_sentence)
    sentence = input()