annual_tax = int(input())
shoes = annual_tax * float(0.6)
outfit = shoes * float(0.8)
ball = outfit / 4
other_needs = ball / 5
total_sum = annual_tax + shoes + outfit \
    + ball + other_needs
print(total_sum)
