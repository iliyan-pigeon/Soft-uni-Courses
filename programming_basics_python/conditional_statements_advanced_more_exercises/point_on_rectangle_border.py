x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
is_border = True
if x == x1 or x == x2:
    if y1 <= y <= y2:
        pass
    else:
        is_border = False
elif y == y1 or y == y2:
    if x1 <= x <= x2:
        pass
    else:
        is_border = False
else:
    is_border = False
if is_border:
    print("Border")
elif not is_border:
    print("Inside / Outside")
