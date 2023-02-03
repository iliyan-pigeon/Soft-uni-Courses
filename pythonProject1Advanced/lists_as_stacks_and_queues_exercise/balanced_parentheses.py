parentheses = input()
parentheses_stack = []
balanced = True
if len(parentheses) % 2 != 0:
    balanced = False
for ch in parentheses:
    if not balanced:
        break
    if ch == "(" or ch == "{" or ch == "[":
        parentheses_stack.append(ch)
    elif ch == ")":
        if parentheses_stack.pop() != "(":
            balanced = False
    elif ch == "}":
        if parentheses_stack.pop() != "{":
            balanced = False
    elif ch == "]":
        if parentheses_stack.pop() != "[":
            balanced = False
if balanced:
    print("YES")
elif not balanced:
    print("NO")




