file_path = input().split(".")
extension = file_path[1]
name = file_path[0].split("\\")[-1]
print(f"File name: {name}")
print(f"File extension: {extension}")
