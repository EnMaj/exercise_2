str = ""
with open("input.txt") as file,open("output.txt", "w+") as file_new:
    for line in file:
        if "\n" in line:
            str+=line[-2:-1]
        else:
            str+=line[-1:]
    file_new.write(str)