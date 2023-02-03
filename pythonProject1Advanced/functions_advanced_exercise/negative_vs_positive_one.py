def separate_and_sum(*args):
    positive = []
    negative = []
    for number in args:
        if number > 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)

    def add_and_evaluate():
        current_result = ""
        current_result += str(sum(negative)) + "\n"
        current_result += str(sum(positive)) + "\n"
        if abs(sum(negative)) > abs(sum(positive)):
            current_result += "The negatives are stronger than the positives"
        else:
            current_result += "The positives are stronger than the negatives"
        return current_result
    return add_and_evaluate()


print(separate_and_sum(1, 2, -3, -4, 65, -98, 12, 57, -84))
