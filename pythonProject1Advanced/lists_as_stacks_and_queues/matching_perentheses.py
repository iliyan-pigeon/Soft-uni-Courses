algebraic_expression = input()
openers = []
for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == "(":
        openers.append(i)
    elif algebraic_expression[i] == ")":
        opener = openers.pop()
        current_expression = algebraic_expression[opener:i+1]
        print(current_expression)


