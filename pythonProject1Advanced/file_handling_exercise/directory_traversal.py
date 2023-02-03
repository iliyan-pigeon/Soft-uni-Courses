import os

directory = input()
extensions = {}
result = ""

for directory_files in os.walk(directory):
    for file in directory_files[2]:
        current_extension = f".{file.split('.')[1]}"
        file_name = f"- - - {file}"
        if current_extension not in extensions:
            extensions[current_extension] = []
        extensions[current_extension].append(file_name)

extensions = sorted(extensions.items(), key=lambda x: x)

for extension in extensions:
    the_extension = extension[0]
    ordered_files = sorted(extension[1])
    result += f"{the_extension}\n"
    for file in ordered_files:
        result += f"{file}\n"

with open("files_directory_traversal/report.txt", "w") as text:
    text.write(result)
