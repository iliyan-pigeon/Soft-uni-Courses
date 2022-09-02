data = input().split()
products = {}
for i in range(0, len(data), 2):
    products[data[i]] = int(data[i+1])
products_to_search = input().split()
for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
 