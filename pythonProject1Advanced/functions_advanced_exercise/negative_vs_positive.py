def separate_and_sum(numbers_list):
    positive = []
    negative = []
    for number in numbers_list:
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


numbers = [int(i) for i in input().split()]
result = separate_and_sum(numbers)
print(result)
