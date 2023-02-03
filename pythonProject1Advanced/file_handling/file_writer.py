file_path = "./my_first_file.txt"
# "w" mode creates new file, and add content to it. If the file already exists, it clears the content and write new one.

file = open(file_path, "w")
file.write("I just created my first file!")
