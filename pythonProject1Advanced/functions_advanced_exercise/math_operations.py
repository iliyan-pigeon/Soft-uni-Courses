def math_operations(*args, **kwargs):
    counter = 1
    result = ''
    args = [float(i) for i in args]
    for arg in args:
        if counter == 1:
            kwargs["a"] += arg
        elif counter == 2:
            kwargs["s"] -= arg
        elif counter == 3:
            if arg != 0 and kwargs["d"] != 0:
                kwargs["d"] /= arg
        elif counter == 4:
            kwargs["m"] *= arg
            counter = 0
        counter += 1
    sorted_elements = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    for key, value in sorted_elements.items():
        result += f"{key}: {value:.1f}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))