def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."


number = int(input())
print(loading_bar(number))