file_path = "./text.txt"
try:
    file = open(file_path, 'r')
    print(file)
except FileNotFoundError:
    print("File not found")