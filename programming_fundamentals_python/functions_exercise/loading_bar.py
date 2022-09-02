def loading_bar(number):
    bar_list = []
    percents_string = int(number / 10) * '%'
    dots_string = int(10 - number / 10) * '.'
    bar_list.append("[" + percents_string)
    bar_list.append(dots_string + ']')
    final_bar = "".join(bar_list)
    if number == 100:
        return f"{number}% Complete!\n{final_bar}"
    return f"{number}% {final_bar}\nStill loading..."


number = int(input())
print(loading_bar(number))

