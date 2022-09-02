repeat_string = lambda letters, number: letters * number


sentence = input()
times = int(input())
print(repeat_string(sentence, times))
