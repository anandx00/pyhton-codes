with open("my_file.txt") as file_object:
    lines =file_object.readlines()
for line in lines:
    print(line.replace("sfdsfs",'dog'))
