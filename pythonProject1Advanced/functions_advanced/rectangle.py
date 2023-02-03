def rectangle(*args):
    def area():
        return args[0] * args[1]

    def perimeter():
        return args[0]*2 + args[1]*2
    result = 0
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return "Enter valid values!"


print(rectangle(2, 10))
