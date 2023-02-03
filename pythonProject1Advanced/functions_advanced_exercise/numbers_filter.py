def even_odd_filter(**kwargs):
    sorted_dicts = {}
    for key, value in kwargs.items():
        if key == "odd":
            sorted_dicts["odd"] = [int(i) for i in value if i % 2 != 0]
        elif key == "even":
            sorted_dicts["even"] = [int(i) for i in value if i % 2 == 0]
    return dict(sorted(sorted_dicts.items(), key=lambda x: len(x[1]), reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
