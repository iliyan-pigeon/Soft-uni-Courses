first_number = int(input())
second_number = int(input())
third_number = int(input())


def positive_negative(n1, n2, n3):
    data = [n1, n2, n3]
    positive = []
    negative = []
    zero = False
    for n in data:
        if n > 0:
            positive.append(n)
        elif n < 0:
            negative.append(n)
        elif n == 0:
            zero = True
    if zero:
        return "zero"
    elif sum(positive) > sum(negative):
        return "positive"
    elif sum(positive) < sum(negative):
        return "negative"
    else:
        return "zero"


print(positive_negative(first_number, second_number, third_number))

