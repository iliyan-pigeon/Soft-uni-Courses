import os


def save_extensions(directory_arg, first_level=False):
    for filename in os.listdir(directory_arg):
        file = os.path.join(directory_arg, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, True)


directory = input()
result = []
extensions = {}

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}\n")

    for file in sorted(files):
        result.append(f"- - - {file}\n")

with open("report.txt", "w") as file:
    file.write("".join(result))