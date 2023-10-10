with open("input.txt") as file, open("output.txt", "w+") as file_new:
    for line in file:
        if line[0]=="A":
            file_new.write(line)

