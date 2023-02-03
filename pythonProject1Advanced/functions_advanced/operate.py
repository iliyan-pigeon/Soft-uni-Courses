def operate(operator: str, *args):
    def multiply():
        result = 1
        for arg in args:
            result *= arg
        return result

    def divide():
        result = args[0]
        for arg in args:
            if arg == args[0]:
                pass
            else:
                result /= arg
        return result

    def add():
        result = 0
        for arg in args:
            result += arg
        return result

    def subtract():
        result = args[0]
        for arg in args:
            if arg == args[0]:
                pass
            else:
                result -= arg
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "/":
        return divide()
    elif operator == "*":
        return multiply()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
