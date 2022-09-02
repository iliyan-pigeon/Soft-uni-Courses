#contribution = input()
#total = 0
#while contribution != "NoMoreMoney":
#    if float(contribution) < 0:
#        print("Invalid operation!")
#        break
#    print(f"Increase: {float(contribution):.2f}")
#    total += float(contribution)
#    contribution = input()
#print(f"Total: {total:.2f}")

contribution = input()
total = 0
while contribution != "NoMoreMoney":
    amount = float(contribution)
    if amount < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {amount:.2f}")
    total += amount
    contribution = input()
print(f"Total: {total:.2f}")