first_number = int(input())
second_number = int(input())
third_number = int(input())


def positive_negative(n1, n2, n3):
    data = [n1, n2, n3]
    zero = False
    negative = False
    count_negative = 0
    for n in data:
        if n == 0:
            zero = True
        elif n < 0:
            if count_negative == 0 or count_negative == 2:
                negative = True
            count_negative += 1
    if zero:
        return "zero"
    elif negative:
        return "negative"
    else:
        return "positive"



print(positive_negative(first_number, second_number, third_number))

