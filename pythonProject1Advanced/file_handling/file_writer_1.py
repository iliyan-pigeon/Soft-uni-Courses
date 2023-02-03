file_path = "./my_first_file.txt"
# "a" mode creates new file, and add content to it. If the file already exists, it adds to the existing content.

file = open(file_path, "a")
file.write("I just created my first file!")
