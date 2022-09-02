def data_type_manipulator(data_type: str, info):
    if data_type == "int":
        return int(info) * 2
    elif data_type == "real":
        return f"{float(info) * 1.5:.2f}"
    elif data_type == "string":
        return f"${info}$"


type_of_data = input()
information = input()
result = data_type_manipulator(type_of_data, information)
print(result)
