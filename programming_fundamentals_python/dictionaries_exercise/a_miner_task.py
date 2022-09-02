command = input()
resources = {}
while command != "stop":
    resource = command
    amount = int(input())
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += amount
    command = input()
for resource, amount in resources.items():
    print(f"{resource} -> {amount}")
    