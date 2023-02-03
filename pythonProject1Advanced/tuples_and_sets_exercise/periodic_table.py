elements_inputs_amount = int(input())
unique_elements = set()
for i in range(elements_inputs_amount):
    current_elements = input().split()
    for element in current_elements:
        unique_elements.add(element)
for element in unique_elements:
    print(element)
    