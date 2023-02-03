from collections import deque


def stock_availability(stock_list, command, *args):
    stock_list = deque(stock_list)

    if command == "delivery":
        for arg in args:
            stock_list.append(arg)

    elif command == "sell":
        if args:
            for arg in args:
                if str(arg).isdigit():
                    for i in range(int(arg)):
                        stock_list.popleft()
                else:
                    while arg in stock_list:
                        stock_list.remove(arg)
        else:
            stock_list.popleft()

    stock_list = list(stock_list)
    return stock_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


