import math

number_easter_breads = int(input())
sugar_packages = 0
flour_packages = 0
total_sugar_grams = 0
total_flour_grams = 0
max_sugar = 0
max_flour = 0
package_sugar_grams = 950
package_flour_grams = 750
for bread in range(number_easter_breads):
    current_sugar = int(input())
    current_flour = int(input())
    total_sugar_grams += current_sugar
    total_flour_grams += current_flour
    if current_sugar > max_sugar:
        max_sugar = current_sugar
    if current_flour > max_flour:
        max_flour = current_flour
sugar_packages = math.ceil(total_sugar_grams / package_sugar_grams)
flour_packages = math.ceil(total_flour_grams / package_flour_grams)
print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")